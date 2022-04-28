from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from src.apps.goods.models import Dish
from src.apps.contact.models import Contact
from src.apps.orders.models import Order, OrderItem, Discount

from .serializers import (
    DishListSerializer,
    DishDetailSerializer,
    ContactListSerializer,
    ContactDetailSerializer,
    DiscountDetailSerializer,
    OrderItemDetailSerializer,
    OrderDetailSerializer
)


class OrderViewSet(viewsets.ModelViewSet):
    """List of all Orders"""

    queryset = Order.objects.all()
    permission_classes = (IsAdminUser,)

    serializer_class = OrderDetailSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    """List of all OrdersItems"""

    queryset = OrderItem.objects.all()
    permission_classes = (IsAdminUser,)

    serializer_class = OrderItemDetailSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    """List of all Discounts"""

    queryset = Discount.objects.all()
    permission_classes = (IsAdminUser,)

    serializer_class = DiscountDetailSerializer


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
