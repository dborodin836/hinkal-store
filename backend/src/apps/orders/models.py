from django.db import models

from src.apps.core.models import TimeStampedAddedByModel, TimeStampedModelMixin
from src.apps.goods.models import Dish
from src.apps.user.models import Customer


class Discount(TimeStampedAddedByModel):
    """
    Discount for all order.

    It also might be called 'promo codes'.
    """

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    discount_word = models.CharField(max_length=100)
    discount_amount = models.PositiveIntegerField()
    # Admin should also be able to add Discounts
    is_active = models.BooleanField(default=False)

    def __repr__(self):
        return (
            f"Discount({self.name}, {self.description}, {self.discount_word}, "
            f"{self.discount_amount}, {repr(self.added_by)}, {self.is_active})"
        )

    def __str__(self):
        return self.name if self.name else self.discount_word


class OrderModifier(TimeStampedAddedByModel):
    """
    Modifier for ALL order.

    Examples: Fast Delivery
             Personal Support
    """

    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=255)

    def __repr__(self):
        return f"OrderModifier({self.title}, {self.descriptions})"

    def __str__(self):
        return self.title


class Order(TimeStampedModelMixin):
    """
    Contains  order from user.

    Need to be managed by stuff, like physically constructed.
    """

    STATUS = (
        ("new", "new order"),
        ("pending", "pending order"),
        ("finished", "finished order"),
        ("canceled", "canceled order"),
    )

    comment = models.TextField(blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    modifier = models.ManyToManyField(OrderModifier, blank=True)
    status = models.CharField(choices=STATUS, default="new", max_length=200)
    ordered_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return (
            f"Order({self.comment}, {self.created_at}, {self.discount}, "
            f"{repr(self.modifier)}, {self.status})"
        )

    def __str__(self):
        return "Order " + str(self.id)


class OrderItem(TimeStampedModelMixin):
    """
    Contains order items.

    Like amount of dish #1 etc.
    """

    item = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="details")

    def __repr__(self):
        return f"OrderItem({repr(self.item)}, {self.amount}, {repr(self.order)})"

    def __str__(self):
        return f"{self.item.title} ({self.amount})"
