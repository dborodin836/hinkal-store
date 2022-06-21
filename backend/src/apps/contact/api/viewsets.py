from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from src.apps.contact.api.serializers import (
    ContactDetailSerializer,
    ContactListSerializer,
)
from src.apps.contact.models import Contact


class ContactViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """All contacts"""

    queryset = Contact.objects.all()
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == "list":
            return ContactListSerializer
        return ContactDetailSerializer
