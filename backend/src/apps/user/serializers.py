from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

from djoser import utils
from djoser.compat import get_user_email, get_user_email_field_name
from djoser.conf import settings
from djoser import serializers as djoser_serializers

from src.apps.user.models import Customer, Vendor


class CustomerSerializer(djoser_serializers.UserSerializer):
    class Meta:
        model = Customer
        fields = tuple(Customer.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
        )
        read_only_fields = (settings.LOGIN_FIELD,)

    def update(self, instance, validated_data):
        email_field = get_user_email_field_name(Customer)
        if settings.SEND_ACTIVATION_EMAIL and email_field in validated_data:
            instance_email = get_user_email(instance)
            if instance_email != validated_data[email_field]:
                instance.is_active = False
                instance.save(update_fields=["is_active"])
        return super().update(instance, validated_data)


class CustomerCreateSerializer(djoser_serializers.UserCreateSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
    }

    class Meta:
        model = Customer
        fields = tuple(Customer.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
        )

    def validate(self, attrs):
        user = Customer(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError({"password": serializer_error["non_field_errors"]})

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = Customer.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user


class CustomerCreatePasswordRetypeSerializer(CustomerCreateSerializer):
    default_error_messages = {
        "password_mismatch": settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["re_password"] = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        self.fields.pop("re_password", None)
        re_password = attrs.pop("re_password")
        attrs = super().validate(attrs)
        if attrs["password"] == re_password:
            return attrs
        else:
            self.fail("password_mismatch")


class CustomerTokenCreateSerializer(serializers.Serializer):
    password = serializers.CharField(required=False, style={"input_type": "password"})

    default_error_messages = {
        "invalid_credentials": settings.CONSTANTS.messages.INVALID_CREDENTIALS_ERROR,
        "inactive_account": settings.CONSTANTS.messages.INACTIVE_ACCOUNT_ERROR,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields[settings.LOGIN_FIELD] = serializers.CharField(required=False)

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(request=self.context.get("request"), **params, password=password)
        if not self.user:
            self.user = Customer.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")


class CustomerFunctionsMixin:
    def get_user(self, is_active=True):
        try:
            user = Customer._default_manager.get(
                is_active=is_active,
                **{self.email_field: self.data.get(self.email_field, "")},
            )
            if user.has_usable_password():
                return user
        except Customer.DoesNotExist:
            pass
        if (
            settings.PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND
            or settings.USERNAME_RESET_SHOW_EMAIL_NOT_FOUND
        ):
            self.fail("email_not_found")


class CustomerSendEmailResetSerializer(serializers.Serializer, CustomerFunctionsMixin):
    default_error_messages = {"email_not_found": settings.CONSTANTS.messages.EMAIL_NOT_FOUND}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.email_field = get_user_email_field_name(Customer)
        self.fields[self.email_field] = serializers.EmailField()


class CustomerUidAndTokenSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    default_error_messages = {
        "invalid_token": settings.CONSTANTS.messages.INVALID_TOKEN_ERROR,
        "invalid_uid": settings.CONSTANTS.messages.INVALID_UID_ERROR,
    }

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        # uid validation have to be here, because validate_<field_name>
        # doesn't work with modelserializer
        try:
            uid = utils.decode_uid(self.initial_data.get("uid", ""))
            self.user = Customer.objects.get(pk=uid)
        except (Customer.DoesNotExist, ValueError, TypeError, OverflowError):
            key_error = "invalid_uid"
            raise ValidationError({"uid": [self.error_messages[key_error]]}, code=key_error)

        is_token_valid = self.context["view"].token_generator.check_token(
            self.user, self.initial_data.get("token", "")
        )
        if is_token_valid:
            return validated_data
        else:
            key_error = "invalid_token"
            raise ValidationError({"token": [self.error_messages[key_error]]}, code=key_error)


class CustomerActivationSerializer(CustomerUidAndTokenSerializer):
    default_error_messages = {"stale_token": settings.CONSTANTS.messages.STALE_TOKEN_ERROR}

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.user.is_active:
            return attrs
        raise exceptions.PermissionDenied(self.error_messages["stale_token"])


class CustomerPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        user = self.context["request"].user or self.user
        # why assert? There are ValidationError / fail everywhere
        assert user is not None

        try:
            validate_password(attrs["new_password"], user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)


class CustomerPasswordRetypeSerializer(CustomerPasswordSerializer):
    re_new_password = serializers.CharField(style={"input_type": "password"})

    default_error_messages = {
        "password_mismatch": settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs["new_password"] == attrs["re_new_password"]:
            return attrs
        else:
            self.fail("password_mismatch")


class CurrentPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"})

    default_error_messages = {
        "invalid_password": settings.CONSTANTS.messages.INVALID_PASSWORD_ERROR
    }

    def validate_current_password(self, value):
        is_password_valid = self.context["request"].user.check_password(value)
        if is_password_valid:
            return value
        else:
            self.fail("invalid_password")


class CustomerUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (settings.LOGIN_FIELD,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username_field = settings.LOGIN_FIELD
        self._default_username_field = Customer.USERNAME_FIELD
        self.fields["new_{}".format(self.username_field)] = self.fields.pop(self.username_field)

    def save(self, **kwargs):
        if self.username_field != self._default_username_field:
            kwargs[Customer.USERNAME_FIELD] = self.validated_data.get(
                "new_{}".format(self.username_field)
            )
        return super().save(**kwargs)


class CustomerUsernameRetypeSerializer(CustomerUsernameSerializer):
    default_error_messages = {
        "username_mismatch": settings.CONSTANTS.messages.USERNAME_MISMATCH_ERROR.format(
            settings.LOGIN_FIELD
        )
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["re_new_" + settings.LOGIN_FIELD] = serializers.CharField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        new_username = attrs[settings.LOGIN_FIELD]
        if new_username != attrs["re_new_{}".format(settings.LOGIN_FIELD)]:
            self.fail("username_mismatch")
        else:
            return attrs


class CustomerTokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("auth_token",)


class CustomerSetPasswordSerializer(CustomerPasswordSerializer, CurrentPasswordSerializer):
    pass


class CustomerSetPasswordRetypeSerializer(
    CustomerPasswordRetypeSerializer, CurrentPasswordSerializer
):
    pass


class CustomerPasswordResetConfirmSerializer(
    CustomerUidAndTokenSerializer, CustomerPasswordSerializer
):
    pass


class CustomerPasswordResetConfirmRetypeSerializer(
    CustomerUidAndTokenSerializer, CustomerPasswordRetypeSerializer
):
    pass


class CustomerUsernameResetConfirmSerializer(
    CustomerUidAndTokenSerializer, CustomerUsernameSerializer
):
    pass


class CustomerUsernameResetConfirmRetypeSerializer(
    CustomerUidAndTokenSerializer, CustomerUsernameRetypeSerializer
):
    pass


class CustomerDeleteSerializer(CurrentPasswordSerializer):
    pass


class CustomerSetUsernameSerializer(CustomerUsernameSerializer, CurrentPasswordSerializer):
    class Meta:
        model = Customer
        fields = (settings.LOGIN_FIELD, "current_password")


class CustomerSetUsernameRetypeSerializer(
    CustomerSetUsernameSerializer, CustomerUsernameRetypeSerializer
):
    pass


class VendorSerializer(djoser_serializers.UserSerializer):
    class Meta:
        model = Vendor
        fields = tuple(Vendor.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
        )
        read_only_fields = (settings.LOGIN_FIELD,)

    def update(self, instance, validated_data):
        email_field = get_user_email_field_name(Vendor)
        if settings.SEND_ACTIVATION_EMAIL and email_field in validated_data:
            instance_email = get_user_email(instance)
            if instance_email != validated_data[email_field]:
                instance.is_active = False
                instance.save(update_fields=["is_active"])
        return super().update(instance, validated_data)


class VendorCreateSerializer(djoser_serializers.UserCreateSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
    }

    class Meta:
        model = Vendor
        fields = tuple(Vendor.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
        )

    def validate(self, attrs):
        user = Vendor(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError({"password": serializer_error["non_field_errors"]})

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = Vendor.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user


class VendorCreatePasswordRetypeSerializer(VendorCreateSerializer):
    default_error_messages = {
        "password_mismatch": settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["re_password"] = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        self.fields.pop("re_password", None)
        re_password = attrs.pop("re_password")
        attrs = super().validate(attrs)
        if attrs["password"] == re_password:
            return attrs
        else:
            self.fail("password_mismatch")


class VendorTokenCreateSerializer(serializers.Serializer):
    password = serializers.CharField(required=False, style={"input_type": "password"})

    default_error_messages = {
        "invalid_credentials": settings.CONSTANTS.messages.INVALID_CREDENTIALS_ERROR,
        "inactive_account": settings.CONSTANTS.messages.INACTIVE_ACCOUNT_ERROR,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields[settings.LOGIN_FIELD] = serializers.CharField(required=False)

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(request=self.context.get("request"), **params, password=password)
        if not self.user:
            self.user = Vendor.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")


class VendorFunctionsMixin:
    def get_user(self, is_active=True):
        try:
            user = Vendor._default_manager.get(
                is_active=is_active,
                **{self.email_field: self.data.get(self.email_field, "")},
            )
            if user.has_usable_password():
                return user
        except Vendor.DoesNotExist:
            pass
        if (
            settings.PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND
            or settings.USERNAME_RESET_SHOW_EMAIL_NOT_FOUND
        ):
            self.fail("email_not_found")


class VendorSendEmailResetSerializer(serializers.Serializer, VendorFunctionsMixin):
    default_error_messages = {"email_not_found": settings.CONSTANTS.messages.EMAIL_NOT_FOUND}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.email_field = get_user_email_field_name(Vendor)
        self.fields[self.email_field] = serializers.EmailField()


class VendorUidAndTokenSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    default_error_messages = {
        "invalid_token": settings.CONSTANTS.messages.INVALID_TOKEN_ERROR,
        "invalid_uid": settings.CONSTANTS.messages.INVALID_UID_ERROR,
    }

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        # uid validation have to be here, because validate_<field_name>
        # doesn't work with modelserializer
        try:
            uid = utils.decode_uid(self.initial_data.get("uid", ""))
            self.user = Vendor.objects.get(pk=uid)
        except (Vendor.DoesNotExist, ValueError, TypeError, OverflowError):
            key_error = "invalid_uid"
            raise ValidationError({"uid": [self.error_messages[key_error]]}, code=key_error)

        is_token_valid = self.context["view"].token_generator.check_token(
            self.user, self.initial_data.get("token", "")
        )
        if is_token_valid:
            return validated_data
        else:
            key_error = "invalid_token"
            raise ValidationError({"token": [self.error_messages[key_error]]}, code=key_error)


class VendorActivationSerializer(VendorUidAndTokenSerializer):
    default_error_messages = {"stale_token": settings.CONSTANTS.messages.STALE_TOKEN_ERROR}

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.user.is_active:
            return attrs
        raise exceptions.PermissionDenied(self.error_messages["stale_token"])


class VendorPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        user = self.context["request"].user or self.user
        # why assert? There are ValidationError / fail everywhere
        assert user is not None

        try:
            validate_password(attrs["new_password"], user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)


class VendorPasswordRetypeSerializer(VendorPasswordSerializer):
    re_new_password = serializers.CharField(style={"input_type": "password"})

    default_error_messages = {
        "password_mismatch": settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs["new_password"] == attrs["re_new_password"]:
            return attrs
        else:
            self.fail("password_mismatch")


class VendorCurrentPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"})

    default_error_messages = {
        "invalid_password": settings.CONSTANTS.messages.INVALID_PASSWORD_ERROR
    }

    def validate_current_password(self, value):
        is_password_valid = self.context["request"].user.check_password(value)
        if is_password_valid:
            return value
        else:
            self.fail("invalid_password")


class VendorUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (settings.LOGIN_FIELD,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username_field = settings.LOGIN_FIELD
        self._default_username_field = Vendor.USERNAME_FIELD
        self.fields["new_{}".format(self.username_field)] = self.fields.pop(self.username_field)

    def save(self, **kwargs):
        if self.username_field != self._default_username_field:
            kwargs[Vendor.USERNAME_FIELD] = self.validated_data.get(
                "new_{}".format(self.username_field)
            )
        return super().save(**kwargs)


class VendorUsernameRetypeSerializer(VendorUsernameSerializer):
    default_error_messages = {
        "username_mismatch": settings.CONSTANTS.messages.USERNAME_MISMATCH_ERROR.format(
            settings.LOGIN_FIELD
        )
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["re_new_" + settings.LOGIN_FIELD] = serializers.CharField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        new_username = attrs[settings.LOGIN_FIELD]
        if new_username != attrs["re_new_{}".format(settings.LOGIN_FIELD)]:
            self.fail("username_mismatch")
        else:
            return attrs


class VendorTokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("auth_token",)


class VendorSetPasswordSerializer(VendorPasswordSerializer, VendorCurrentPasswordSerializer):
    pass


class VendorSetPasswordRetypeSerializer(
    VendorPasswordRetypeSerializer, VendorCurrentPasswordSerializer
):
    pass


class VendorPasswordResetConfirmSerializer(VendorUidAndTokenSerializer, VendorPasswordSerializer):
    pass


class VendorPasswordResetConfirmRetypeSerializer(
    VendorUidAndTokenSerializer, VendorPasswordRetypeSerializer
):
    pass


class VendorUsernameResetConfirmSerializer(VendorUidAndTokenSerializer, VendorUsernameSerializer):
    pass


class VendorUsernameResetConfirmRetypeSerializer(
    VendorUidAndTokenSerializer, VendorUsernameRetypeSerializer
):
    pass


class VendorDeleteSerializer(VendorCurrentPasswordSerializer):
    pass


class VendorSetUsernameSerializer(VendorUsernameSerializer, VendorCurrentPasswordSerializer):
    class Meta:
        model = Vendor
        fields = (settings.LOGIN_FIELD, "current_password")


class VendorSetUsernameRetypeSerializer(
    VendorSetUsernameSerializer, VendorUsernameRetypeSerializer
):
    pass
