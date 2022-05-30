from rest_framework import serializers

from src.apps.orders.models import Discount, Order, OrderItem


class OrderItemDetailSerializer(serializers.ModelSerializer):
    """Detailed OrderItem"""

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    """Detailed Order"""

    class Meta:
        model = Order
        fields = "__all__"


class DiscountDetailSerializer(serializers.ModelSerializer):
    """Detailed Discount"""

    class Meta:
        model = Discount
        fields = "__all__"
