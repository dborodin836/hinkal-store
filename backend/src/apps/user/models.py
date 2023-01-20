from django.contrib.auth.models import User
from django.db import models


class Country(models.Model):
    """Table for countries and their codes"""

    fullname = models.CharField(max_length=100)
    code = models.CharField(max_length=4)

    def __repr__(self):
        return f"Country({self.fullname}), {self.code}"

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class UserAddress(models.Model):
    """Contains user's addresses"""

    # Make sense to make another table for streets, cities, house number. Just in case user
    # has houses in different cities. Or we can change this model to Many-to-One type...
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50)
    postal_code = models.PositiveIntegerField()
    county = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return (
            f"UserAddress({self.address_1}, {self.address_2}, {self.city}, {self.postal_code}, "
            f"{repr(self.county)})"
        )

    def __str__(self):
        return f"Customer {str(self.customer.username)}'s addresses"

    class Meta:
        verbose_name = "User's Address"
        verbose_name_plural = "User's Addresses"


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
    address = models.OneToOneField(UserAddress, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f"Customer({self.phone}, {self.address})"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
