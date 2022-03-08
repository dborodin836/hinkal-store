from django.urls import include, path
from rest_framework import routers

from .views import DishViewSet

router = routers.DefaultRouter()
router.register(r'dish', DishViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
