from django.contrib.auth.models import User
from django.db import models

from src.apps.core.models import TimeStampedAddedByModel
from src.apps.goods.managers import DishManager


class Category(TimeStampedAddedByModel):
    """
    Categories for products.
    """

    name = models.CharField(max_length=50)

    def __repr__(self):
        return f"Category({self.name})"

    def __str__(self):
        return self.name


class Dish(TimeStampedAddedByModel):
    """
    Contains dishes added by Vendors.
    """

    objects = DishManager()

    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description", blank=True)
    image = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        verbose_name="Image",
        default="default/not-found.png",
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    is_active = models.BooleanField(default=True, verbose_name="Available for users?")
    times_bought = models.IntegerField(default=0, verbose_name="Times bought")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return (
            f"Dish({self.title}, {self.description}, {self.image}, {self.created_at}, "
            f"{repr(self.added_by)}, {self.price}, {self.is_active}, {self.times_bought}, {self.category})"
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"
