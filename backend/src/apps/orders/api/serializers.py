from rest_framework import serializers

from src.apps.orders.models import Discount, Order, OrderItem


class OrderItemDetailSerializer(serializers.ModelSerializer):
    """Detailed OrderItem"""

    class Meta:
        model = OrderItem
        fields = ("id", "item", "amount", "order")


class OrderDetailSerializer(serializers.ModelSerializer):
    """Detailed Order"""

    details = OrderItemDetailSerializer(many=True)

    def create(self, validated_data):
        order_items = validated_data.pop("details")
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(order=order, **item)
        return order

    class Meta:
        model = Order
        fields = (
            "id",
            "comment",
            "ordered_date",
            "discount",
            "modifier",
            "status",
            "ordered_by",
            "details",
        )


class DiscountDetailSerializer(serializers.ModelSerializer):
    """Detailed Discount"""

    class Meta:
        model = Discount
        fields = (
            "id",
            "name",
            "description",
            "discount_word",
            "discount_amount",
            "added_by",
            "is_active",
        )
