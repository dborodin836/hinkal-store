from django.db import models

from datetime import datetime as dt

from src.apps.goods.models import Dish
from src.apps.user.models import Vendor, Customer


class Discount(models.Model):
    """Discount for all order"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    discount_word = models.CharField(max_length=100)
    discount_amount = models.PositiveIntegerField()
    # Admin should also add Discounts
    added_by = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class OrderModifier(models.Model):
    """Modifier for ALL order"""
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Order(models.Model):
    """Contains order from user"""

    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order')
    )

    ordered_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(default='')
    ordered_date = models.DateTimeField(default=dt.now())
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    modifier = models.ManyToManyField(OrderModifier)
    status = models.CharField(choices=STATUS, default='new', max_length=200)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    """Contains order items"""
    item = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item.title} ({self.amount})'
