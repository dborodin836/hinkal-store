from django.urls import include, path
from rest_framework import routers

from src.apps.contact.api.viewsets import ContactViewSet
from src.apps.goods.api.viewsets import DishViewSet
from src.apps.orders.api.viewsets import DiscountViewSet, OrderItemViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r"dish", DishViewSet)
router.register(r"contact", ContactViewSet)
router.register(r"order", OrderViewSet)
router.register(r"order-item", OrderItemViewSet)
router.register(r"discount", DiscountViewSet)

urlpatterns = [path(r"", include(router.urls))]
