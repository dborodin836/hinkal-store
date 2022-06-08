from rest_framework import serializers

from src.apps.goods.models import Dish


class DishListSerializer(serializers.ModelSerializer):
    """List of all dishes"""

    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)  # type: ignore

    class Meta:
        model = Dish
        exclude = ("added_date",)


class DishDetailSerializer(serializers.ModelSerializer):
    """Detailed dish (all fields)"""

    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)  # type: ignore

    class Meta:
        model = Dish
        fields = "__all__"
