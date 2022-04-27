from django.core.management.base import BaseCommand, CommandError

from goods.models import Dish
from user.models import Customer, Vendor
from contact.models import Contact
from orders.models import Discount, Order, OrderItem, OrderModifier


class Command(BaseCommand):
    help = 'Clears Customers, Vendors, Dishes, etc.'

    @staticmethod
    def _clear_db(model=None) -> None:
        models = model or (Customer, Vendor, Dish, Contact, Discount, Order, OrderItem, OrderModifier)
        models = list(models)
        for model in models:
            model.objects.all().delete()

    def add_arguments(self, parser):
        ...

    def handle(self, *args, **options):
        self._clear_db()
        self.stdout.write("DB is clear now!")
