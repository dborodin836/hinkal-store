from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (
    IsAdminUser,
    DjangoModelPermissions,
    AllowAny,
)
from rest_framework.response import Response

from src.apps.core.permissions import Author
from src.apps.orders.api.serializers import (
    DiscountDetailSerializer,
    OrderDetailSerializer,
    OrderItemDetailSerializer,
    DiscountPublicSerializer,
)
from src.apps.orders.models import Discount, Order, OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    """List of all Orders"""

    queryset = Order.objects.all()
    permission_classes = (DjangoModelPermissions & Author,)

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


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_discount_by_name(request, code):
    """
    Get public discount data by discount word.
    """
    discount = get_object_or_404(Discount, discount_word=code, is_active=True)
    serializer = DiscountPublicSerializer(discount, many=False)
    return Response(serializer.data)
