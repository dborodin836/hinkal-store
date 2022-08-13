# mypy: ignore-errors
from django.core.management import call_command
from rest_framework.test import APITestCase

from src.apps.core.decorators import hide_stdout
from src.apps.core.testing.api_clients import CustomerAPIClient, VendorAPIClient
from src.apps.goods.models import Dish, Category


class OrderRetrieveAPITest(APITestCase):
    TEST_CUSTOMER_PASSWORD = "customer"
    TEST_CUSTOMER_USERNAME = "customerpass"

    TEST_VENDOR_PASSWORD = "vendor"
    TEST_VENDOR_USERNAME = "vendorpass"

    base_url = "http://localhost:8000/api/order/"

    @classmethod
    @hide_stdout
    def setUpTestData(cls) -> None:
        call_command("loaddata", "fixtures/groups.json", app_label="auth")
        cls.customerClient = CustomerAPIClient(  # type: ignore
            username=cls.TEST_CUSTOMER_USERNAME, password=cls.TEST_CUSTOMER_PASSWORD
        )
        cls.vendorClient = VendorAPIClient(
            username=cls.TEST_VENDOR_USERNAME, password=cls.TEST_VENDOR_PASSWORD
        )

    def setUp(self) -> None:
        self.category = Category.objects.create(name="Dish")

        self.dish = Dish.objects.create(
            title="test1",
            description="",
            price=699,
            category=self.category,
            added_by=self.vendorClient.user,
        )

        self.data = {
            "comment": "1313",
            "details": [
                {
                    "item": self.dish.id,
                    "amount": 5,
                }
            ],
            "ordered_by": self.customerClient.id,
        }

    def test_retrieve_created(self):
        response = self.customerClient.post(self.base_url, data=self.data, format="json")
        self.assertEqual(response.status_code, 201, msg="Couldn't create order.")
        url = self.base_url + str(response.data["id"]) + "/"
        response_author = self.customerClient.get(url)
        self.assertEqual(response_author.status_code, 200)

    def test_retrieve_order_for_another_user(self):
        response = self.customerClient.post(self.base_url, data=self.data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["status"], "new")
        self.assertEqual(response.data["ordered_by"], self.customerClient.id)
        another_customer_client = CustomerAPIClient(  # type: ignore
            username="sometestname", password="somepass"
        )
        assert another_customer_client.id != self.customerClient.id, "Must be different users!"
        response2 = another_customer_client.get(self.base_url + str(response.data["id"]) + "/")
        self.assertIn(response2.status_code, [403, 401])
