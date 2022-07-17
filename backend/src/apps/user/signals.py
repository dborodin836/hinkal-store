from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver


from src.apps.user.models import Customer, Vendor


@receiver(post_save, sender=Customer)
def add_default_customer_group(sender, instance: Customer, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name="Customer"))


@receiver(post_save, sender=Vendor)
def add_default_vendor_group(sender, instance: Vendor, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name="Vendor"))
