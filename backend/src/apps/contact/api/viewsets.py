from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from src.apps.contact.api.serializers import (
    ContactDetailSerializer,
    ContactListSerializer,
)
from src.apps.contact.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    """All contacts"""

    queryset = Contact.objects.all()
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == "list":
            return ContactListSerializer
        return ContactDetailSerializer
