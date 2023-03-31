from django.contrib.auth.models import User
from django.db import models


class Vendor(User):
    """Model for vendors"""

    biography = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50, default="")

    def __repr__(self):
        return f"Vendor({self.biography}, {self.phone}, {self.company_name})"

    def __str__(self):
        return self.company_name or self.username

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"


class Customer(User):
    """Model for regular users"""

    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=256, null=True)

    def __repr__(self):
        return f"Customer({self.phone}, {self.address})"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
