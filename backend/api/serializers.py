from rest_framework import serializers

from goods.models import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('title', 'description')
