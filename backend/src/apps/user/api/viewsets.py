from djoser.views import UserViewSet

from djoser.conf import settings
from src.apps.user.models import Customer, Vendor
from src.apps.user.serializers import (
    CustomerCreateSerializer,
    CustomerCreatePasswordRetypeSerializer,
    CustomerDeleteSerializer,
    CustomerActivationSerializer,
    CustomerSendEmailResetSerializer,
    CustomerSerializer,
    CustomerUsernameResetConfirmSerializer,
    CustomerUsernameResetConfirmRetypeSerializer,
    CustomerSetUsernameSerializer,
    CustomerSetUsernameRetypeSerializer,
    CustomerSetPasswordSerializer,
    VendorSetPasswordRetypeSerializer,
    CustomerPasswordResetConfirmSerializer,
    CustomerPasswordResetConfirmRetypeSerializer,
    VendorSerializer,
    VendorCreatePasswordRetypeSerializer,
    VendorCreateSerializer,
    VendorDeleteSerializer,
    VendorActivationSerializer,
    VendorSendEmailResetSerializer,
    VendorPasswordResetConfirmRetypeSerializer,
    VendorPasswordResetConfirmSerializer,
    VendorSetPasswordSerializer,
    VendorSetUsernameRetypeSerializer,
    VendorSetUsernameSerializer,
    VendorUsernameResetConfirmRetypeSerializer,
    VendorUsernameResetConfirmSerializer,
)


class CustomerViewSet(UserViewSet):
    """
    ViewSet that should be used for all action related to Customer instance.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        if self.action == "create":
            if settings.USER_CREATE_PASSWORD_RETYPE:
                return CustomerCreatePasswordRetypeSerializer
            return CustomerCreateSerializer
        elif self.action == "destroy" or (
            self.action == "me" and self.request and self.request.method == "DELETE"
        ):
            return CustomerDeleteSerializer
        elif self.action == "activation":
            return CustomerActivationSerializer
        elif self.action == "resend_activation":
            return CustomerSendEmailResetSerializer
        elif self.action == "reset_password":
            return CustomerSendEmailResetSerializer
        elif self.action == "reset_password_confirm":
            if settings.PASSWORD_RESET_CONFIRM_RETYPE:
                return CustomerPasswordResetConfirmRetypeSerializer
            return CustomerPasswordResetConfirmSerializer
        elif self.action == "set_password":
            if settings.SET_PASSWORD_RETYPE:
                return VendorSetPasswordRetypeSerializer
            return CustomerSetPasswordSerializer
        elif self.action == "set_username":
            if settings.SET_USERNAME_RETYPE:
                return CustomerSetUsernameRetypeSerializer
            return CustomerSetUsernameSerializer
        elif self.action == "reset_username":
            return CustomerSendEmailResetSerializer
        elif self.action == "reset_username_confirm":
            if settings.USERNAME_RESET_CONFIRM_RETYPE:
                return CustomerUsernameResetConfirmRetypeSerializer
            return CustomerUsernameResetConfirmSerializer
        elif self.action == "me":
            return CustomerSerializer

        return self.serializer_class


class VendorViewSet(UserViewSet):
    """
    ViewSet that should be used for all action related to Vendor instance.
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = settings.PERMISSIONS.user
    lookup_field = settings.USER_ID_FIELD

    def get_serializer_class(self):
        if self.action == "create":
            if settings.USER_CREATE_PASSWORD_RETYPE:
                return VendorCreatePasswordRetypeSerializer
            return VendorCreateSerializer
        elif self.action == "destroy" or (
            self.action == "me" and self.request and self.request.method == "DELETE"
        ):
            return VendorDeleteSerializer
        elif self.action == "activation":
            return VendorActivationSerializer
        elif self.action == "resend_activation":
            return VendorSendEmailResetSerializer
        elif self.action == "reset_password":
            return VendorSendEmailResetSerializer
        elif self.action == "reset_password_confirm":
            if settings.PASSWORD_RESET_CONFIRM_RETYPE:
                return VendorPasswordResetConfirmRetypeSerializer
            return VendorPasswordResetConfirmSerializer
        elif self.action == "set_password":
            if settings.SET_PASSWORD_RETYPE:
                return VendorSetPasswordRetypeSerializer
            return VendorSetPasswordSerializer
        elif self.action == "set_username":
            if settings.SET_USERNAME_RETYPE:
                return VendorSetUsernameRetypeSerializer
            return VendorSetUsernameSerializer
        elif self.action == "reset_username":
            return VendorSendEmailResetSerializer
        elif self.action == "reset_username_confirm":
            if settings.USERNAME_RESET_CONFIRM_RETYPE:
                return VendorUsernameResetConfirmRetypeSerializer
            return VendorUsernameResetConfirmSerializer
        elif self.action == "me":
            return VendorSerializer

        return self.serializer_class
