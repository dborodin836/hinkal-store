from django.core.management.base import BaseCommand

from src.apps.contact.models import Contact
from src.apps.goods.models import Dish
from src.apps.orders.models import Discount, Order, OrderItem, OrderModifier
from src.apps.user.models import Customer, Vendor


class Command(BaseCommand):
    help = "Clears Customers, Vendors, Dishes, etc."

    @staticmethod
    def _clear_db(model=None) -> None:
        all_models = (
            Customer,
            Vendor,
            Dish,
            Contact,
            Discount,
            Order,
            OrderItem,
            OrderModifier,
        )
        models = model or all_models
        models = list(models)
        for model_ in models:
            model_.objects.all().delete()

    def add_arguments(self, parser):
        ...

    def handle(self, *args, **options):
        self._clear_db()
        self.stdout.write("DB is clear now!")
