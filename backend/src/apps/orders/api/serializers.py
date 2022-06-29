from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from src.apps.orders.models import Discount, Order, OrderItem


class OrderItemDetailSerializer(serializers.ModelSerializer):
    """Detailed OrderItem"""

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    """Detailed Order"""

    details = OrderItemDetailSerializer(many=True)

    def create(self, validated_data):
        order_items = validated_data.pop('details')
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(order=order, **item)
        return order

    class Meta:
        model = Order
        fields = "__all__"


class DiscountDetailSerializer(serializers.ModelSerializer):
    """Detailed Discount"""

    class Meta:
        model = Discount
        fields = "__all__"
