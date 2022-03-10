from django.contrib.auth.models import User
from rest_framework import serializers

from goods.models import Dish
from contact.models import Contact


class DishListSerializer(serializers.ModelSerializer):
    """List of all dishes"""
    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Dish
        exclude = (
            'added_date',
            )


class DishDetailSerializer(serializers.ModelSerializer):
    """Detailed dish (all fields)"""
    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)

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
