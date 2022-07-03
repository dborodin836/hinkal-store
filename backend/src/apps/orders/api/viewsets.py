from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from src.apps.orders.api.serializers import (
    DiscountDetailSerializer,
    OrderDetailSerializer,
    OrderItemDetailSerializer,
)
from src.apps.orders.models import Discount, Order, OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    """List of all Orders"""

    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)

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
