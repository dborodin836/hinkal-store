from datetime import datetime as dt

from django.db import models

from src.apps.goods.models import Dish
from src.apps.user.models import Customer, Vendor


class Discount(models.Model):
    """
    Discount for all order.

    It also might be called 'promo codes'.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    discount_word = models.CharField(max_length=100)
    discount_amount = models.PositiveIntegerField()
    # Admin should also be able to add Discounts
    added_by = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name if self.name else self.discount_word


class OrderModifier(models.Model):
    """
    Modifier for ALL order.

    Examples: Fast Delivery
             Personal Support
    """
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TemporaryOrder(models.Model):
    """
    Contains order that wasn't passed to constructing service (physically constructed).
    """

    ordered_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Temporary order {self.id}'


class Order(TemporaryOrder):
    """
    Contains  order from user.

    Need to be managed by stuff, like physically constructed.
    """

    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order'),
        ('canceled', 'canceled order')
    )

    comment = models.TextField(blank=True)
    ordered_date = models.DateTimeField(default=dt.now)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    modifier = models.ManyToManyField(OrderModifier, blank=True)
    status = models.CharField(choices=STATUS, default='new', max_length=200)

    def __str__(self):
        return 'Order ' + str(self.id)


class OrderItem(models.Model):
    """
    Contains order items.

    Like amount of dish #1 etc.
    """
    item = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(TemporaryOrder, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item.title} ({self.amount})'
