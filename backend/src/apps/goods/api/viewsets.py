from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from src.apps.goods.api.serializers import DishListSerializer, DishDetailSerializer
from src.apps.goods.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    """List of all dishes"""

    queryset = Dish.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "list":
            return DishListSerializer
        return DishDetailSerializer
