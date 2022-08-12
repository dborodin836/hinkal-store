from djoser.views import UserViewSet

from djoser.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import action

from src.apps.user.models import Customer, Vendor
from src.apps.user.serializers import (
    CustomerCreateSerializer,
    CustomerCreatePasswordRetypeSerializer,
    CustomerDeleteSerializer,
    CustomerSerializer,
    VendorSerializer,
    VendorCreatePasswordRetypeSerializer,
    VendorCreateSerializer,
    VendorDeleteSerializer,
)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet that should be used for all action related to Customer instance.
    """

    user_view_set = UserViewSet()  # type: ignore
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        self.user_view_set.action = self.action
        if self.action == "create":
            if settings.USER_CREATE_PASSWORD_RETYPE:
                return CustomerCreatePasswordRetypeSerializer
            return CustomerCreateSerializer
        elif self.action == "destroy" or (
            self.action == "me" and self.request and self.request.method == "DELETE"
        ):
            return CustomerDeleteSerializer
        elif self.action == "me":
            return CustomerSerializer

        return self.serializer_class

    def permission_denied(self, request, **kwargs):
        self.user_view_set.request = self.request
        self.user_view_set.permission_denied(request, **kwargs)

    def get_queryset(self):
        self.user_view_set.action = self.action
        self.user_view_set.request = self.request
        return self.user_view_set.get_queryset()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = settings.PERMISSIONS.user_create
        elif self.action == "destroy" or (
            self.action == "me" and self.request and self.request.method == "DELETE"
        ):
            self.permission_classes = settings.PERMISSIONS.user_delete
        return super().get_permissions()

    def get_instance(self):
        self.user_view_set.request = self.request
        return self.user_view_set.get_instance()

    def perform_create(self, serializer):
        self.user_view_set.request = self.request
        self.user_view_set.perform_create(serializer)

    def perform_update(self, serializer):
        self.user_view_set.request = self.request
        self.user_view_set.perform_update(serializer)

    def destroy(self, request, *args, **kwargs):
        self.user_view_set.request = self.request
        self.user_view_set.destroy(request, *args, **kwargs)

    @action(["get", "put", "patch", "delete"], detail=False)
    def me(self, request, *args, **kwargs):
        self.user_view_set.request = self.request
        self.user_view_set.me(request, *args, **kwargs)


class VendorViewSet(UserViewSet):
    """
    ViewSet that should be used for all action related to Vendor instance.
    """

    user_view_set = UserViewSet()  # type: ignore
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get_serializer_class(self):
        self.user_view_set.action = self.action
        if self.action == "create":
            if settings.USER_CREATE_PASSWORD_RETYPE:
                return VendorCreatePasswordRetypeSerializer
            return VendorCreateSerializer
        elif self.action == "destroy" or (
            self.action == "me" and self.request and self.request.method == "DELETE"
        ):
            return VendorDeleteSerializer
        elif self.action == "me":
            return VendorSerializer

        return self.serializer_class

    def permission_denied(self, request, **kwargs):
        self.user_view_set.request = self.request
        self.user_view_set.permission_denied(request, **kwargs)

    def get_queryset(self):
        self.user_view_set.action = self.action
        self.user_view_set.request = self.request
        return self.user_view_set.get_queryset()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = settings.PERMISSIONS.user_create
        elif self.action == "destroy" or (
            self.action == "me" and self.request and self.request.method == "DELETE"
        ):
            self.permission_classes = settings.PERMISSIONS.user_delete
        return super().get_permissions()

    def get_instance(self):
        self.user_view_set.request = self.request
        return self.user_view_set.get_instance()

    def perform_create(self, serializer):
        self.user_view_set.request = self.request
        self.user_view_set.perform_create(serializer)

    def perform_update(self, serializer):
        self.user_view_set.request = self.request
        self.user_view_set.perform_update(serializer)

    def destroy(self, request, *args, **kwargs):
        self.user_view_set.request = self.request
        self.user_view_set.destroy(request, *args, **kwargs)

    @action(["get", "put", "patch", "delete"], detail=False)
    def me(self, request, *args, **kwargs):
        self.user_view_set.request = self.request
        self.user_view_set.me(request, *args, **kwargs)
