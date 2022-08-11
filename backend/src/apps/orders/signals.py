from django.db.models.signals import post_save
from django.dispatch import receiver

from src.apps.orders.models import OrderItem


@receiver(post_save, sender=OrderItem)
def increase_time_sold_dish(sender, instance: OrderItem, created, **kwargs):
    """
    Updates amount of times bought for every dish in order.
    """
    if created:
        dish = instance.item
        dish.times_bought += 1  # type: ignore
        dish.save()  # type: ignore
