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

    # Used to convert requested category to order_by parameter.
    ORDERING_DICT = {
        "popular": "-times_bought",
        "newest": "-added_date",
        "max_price": "-price",
        "min_price": "price",
    }

    def get_queryset(self):
        queryset = Dish.objects.all()

        if self.request.GET.get("id"):
            queryset = queryset.filter(pk__in=self.request.GET.get("id").split(","))

        if self.request.GET.get("query_keyword"):
            queryset = queryset.filter(title__icontains=self.request.GET.get("query_keyword"))

        if self.request.GET.get("filtered_category"):
            queryset = queryset.filter(
                category__dish__title=self.request.GET.get("filtered_category")
            )

        if self.request.GET.get("ordering"):
            queryset = queryset.order_by(self.ORDERING_DICT[self.request.GET.get("ordering")])
        return queryset


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
