from rest_framework import serializers

from src.apps.contact.models import Contact
from src.apps.goods.models import Dish
from src.apps.orders.models import Discount, Order, OrderItem


class DishListSerializer(serializers.ModelSerializer):
    """List of all dishes"""
    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)  # type: ignore

    class Meta:
        model = Dish
        exclude = (
            'added_date',
        )


class DishDetailSerializer(serializers.ModelSerializer):
    """Detailed dish (all fields)"""
    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)  # type: ignore

    class Meta:
        model = Dish
        fields = '__all__'


class ContactListSerializer(serializers.ModelSerializer):
    """List of all contacts"""

    class Meta:
        model = Contact
        fields = ('id', 'subject', 'message')


class ContactDetailSerializer(serializers.ModelSerializer):
    """Detailed ContactMe"""

    class Meta:
        model = Contact
        fields = '__all__'


class DiscountDetailSerializer(serializers.ModelSerializer):
    """Detailed Discount"""

    class Meta:
        model = Discount
        fields = '__all__'


class OrderItemDetailSerializer(serializers.ModelSerializer):
    """Detailed OrderItem"""

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    """Detailed Order"""

    class Meta:
        model = Order
        fields = '__all__'
