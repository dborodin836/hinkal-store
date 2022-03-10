from django.urls import path, include
from rest_framework import routers

from .views import DishViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'dish', DishViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
