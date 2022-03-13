from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from datetime import datetime as dt

from goods.models import Dish


class OrderItem(models.Model):
    """Contains order items"""
    item = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.item.title} ({self.amount})'


class Discount(models.Model):
    """Discount for all order"""
    discount_word = models.CharField(max_length=100)
    discount_amount = models.PositiveIntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.discount_word


class OrderModifier(models.Model):
    """Modifier for ALL order"""
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Order(models.Model):
    """Contains order from user"""
    ordered_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem, blank=True)
    comment = models.TextField()
    ordered_date = models.DateTimeField(default=dt.now())
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    modifier = models.ManyToManyField(OrderModifier)

    def __str__(self):
        return str(self.id)
