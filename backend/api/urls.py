from django.urls import path, include
from rest_framework import routers

from .views import (
    DishViewSet,
    ContactViewSet,
    OrderViewSet,
    OrderItemViewSet,
    DiscountViewSet
)

router = routers.DefaultRouter()
router.register(r'dish', DishViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order-item', OrderItemViewSet)
router.register(r'discount', DiscountViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
