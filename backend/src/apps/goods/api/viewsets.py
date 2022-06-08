from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from src.apps.goods.api.serializers import DishDetailSerializer, DishListSerializer
from src.apps.goods.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    """
    List of all dishes.
    """

    queryset = Dish.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == "list":
            return DishListSerializer
        return DishDetailSerializer


class BestSellingDishesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Returns best selling dishes.
    """

    serializer_class = DishListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        amount = int(self.request.query_params.get("limit", 10))
        queryset = Dish.objects.best_selling_active(amount)
        return queryset
