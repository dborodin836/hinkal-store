from rest_framework.routers import DefaultRouter

from .viewsets import CustomerViewSet, VendorViewSet

router = DefaultRouter()
router.register("customers", CustomerViewSet)

router.register("vendors", VendorViewSet)
