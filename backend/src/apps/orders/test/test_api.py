# mypy: ignore-errors
import io
from contextlib import redirect_stdout

from django.core.management import call_command
from rest_framework.test import APITestCase

from src.apps.core.testing.api_clients import CustomerAPIClient, VendorAPIClient
from src.apps.goods.models import Dish, Category


class OrderAPITest(APITestCase):
    TEST_CUSTOMER_PASSWORD = "customer"
    TEST_CUSTOMER_USERNAME = "customerpass"

    TEST_VENDOR_PASSWORD = "vendor"
    TEST_VENDOR_USERNAME = "vendorpass"

    base_url = "http://localhost:8000/api/order/"

    @classmethod
    def setUpTestData(cls) -> None:
        with redirect_stdout(io.StringIO()):
            call_command("loaddata", "fixtures/groups.json", app_label="auth")
        cls.customerClient = CustomerAPIClient(  # type: ignore
            username=cls.TEST_CUSTOMER_USERNAME, password=cls.TEST_CUSTOMER_PASSWORD
        )
        cls.vendorClient = VendorAPIClient(
            username=cls.TEST_VENDOR_USERNAME, password=cls.TEST_VENDOR_PASSWORD
        )

    def test_create_order_single_position(self):
        category = Category.objects.create(name="Dish")
        dish = Dish.objects.create(
            title="test1",
            description="",
            price=699,
            category=category,
            added_by=self.vendorClient.user,
        )

        data = {
            "comment": "1313",
            "details": [
                {
                    "item": dish.id,
                    "amount": 5,
                }
            ],
            "ordered_by": self.customerClient.id,
        }
        response = self.customerClient.post(self.base_url, data=data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["status"], "new")
        self.assertEqual(response.data["ordered_by"], self.customerClient.id)
        self.assertEqual(Dish.objects.get(id=dish.id).times_bought, 1)

        self.customerClient.post(self.base_url, data=data, format="json")
        self.assertEqual(Dish.objects.get(id=dish.id).times_bought, 2)
