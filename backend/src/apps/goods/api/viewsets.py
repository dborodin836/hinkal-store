from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser
from rest_framework.response import Response

from src.apps.core.permissions import Author
from src.apps.goods.api.serializers import (
    DishDetailSerializer,
    DishListSerializer,
    DishCreateSerializer,
)
from src.apps.goods.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    """
    List of all dishes.
    """

    queryset = Dish.objects.all()
    permission_classes = ((IsAdminUser | Author) & DjangoModelPermissionsOrAnonReadOnly,)

    def create(self, request, *args, **kwargs):
        """
        Verify that the POST has the request user as the obj.author
        """
        if request.data["added_by"] == str(request.user.id) or request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        return Response(status=403)

    def get_serializer_class(self):
        if self.action == "list":
            return DishListSerializer
        if self.action == "create":
            return DishCreateSerializer
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
