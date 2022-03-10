from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from goods.models import Dish
from contact.models import Contact
from .serializers import (
    DishListSerializer,
    DishDetailSerializer,
    ContactListSerializer,
    ContactDetailSerializer
)


class DishViewSet(viewsets.ModelViewSet):
    """List of all dishes"""

    queryset = Dish.objects.all()
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return DishListSerializer
        return DishDetailSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """All contacts"""

    queryset = Contact.objects.all()
    permission_classes = (IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ContactListSerializer
        return ContactDetailSerializer
