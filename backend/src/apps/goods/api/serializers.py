from rest_framework import serializers

from src.apps.goods.models import Dish


class DishListSerializer(serializers.ModelSerializer):
    """List of all dishes"""

    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)  # type: ignore

    class Meta:
        model = Dish
        fields = (
            "id",
            "title",
            "image",
            "price",
            "added_by"
        )


class DishDetailSerializer(serializers.ModelSerializer):
    """Detailed dish (all fields)"""

    added_by = serializers.SlugRelatedField(slug_field="username", read_only=True)  # type: ignore

    class Meta:
        model = Dish
        fields = (
            "id",
            "title",
            "description",
            "image",
            "added_date",
            "added_by",
            "price",
            "is_active",
            "times_bought",
            "category",
        )
