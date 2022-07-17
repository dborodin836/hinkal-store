# mypy: ignore-errors
import io

from django.core.management import call_command
from rest_framework.test import APITestCase
from contextlib import redirect_stdout

from src.apps.core.testing.api_clients import CustomerAPIClient, AdminAPIClient, VendorAPIClient
from src.apps.goods.models import Dish, Category

from src.apps.core.testing.factories import VendorFactory


class CustomerDishAPITest(APITestCase):
    TEST_VENDOR_USERNAME = "vendor"
    TEST_VENDOR_PASSWORD = "vendorpass"

    TEST_CUSTOMER_USERNAME = "customer"
    TEST_CUSTOMER_PASSWORD = "customerpass"

    TEST_ADMIN_USERNAME = "admin"
    TEST_ADMIN_PASSWORD = "adminpass"

    base_url = "http://localhost:8000/api/dish/"
    detailed_url = base_url + "3/"

    @classmethod
    def setUpTestData(cls) -> None:
        with redirect_stdout(io.StringIO()):
            call_command("loaddata", "fixtures/groups.json", app_label="auth")

        cls.clientAdmin = AdminAPIClient(
            username=cls.TEST_ADMIN_USERNAME, password=cls.TEST_ADMIN_PASSWORD
        )
        cls.clientVendor = VendorAPIClient(
            username=cls.TEST_VENDOR_USERNAME, password=cls.TEST_VENDOR_PASSWORD
        )

        cls.clientCustomer = CustomerAPIClient(
            username=cls.TEST_CUSTOMER_USERNAME, password=cls.TEST_CUSTOMER_PASSWORD
        )

    def setUp(self) -> None:
        category = Category.objects.create(name="Dish")

        self.data = {
            "title": "test1",
            "price": 699,
            "added_by": self.clientVendor.id,
        }

        self.data_updated = {
            "title": "test1update",
            "price": 899,
        }

        self.dish = Dish.objects.create(
            title="test1",
            description="",
            price=699,
            category=category,
            added_by=self.clientVendor.user,
        )

    def test_get_list_unauthorized(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_get_detail_unauthorized(self):
        response = self.client.get(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 200)

    def test_get_list_admin(self):
        response = self.clientAdmin.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_get_detail_admin(self):
        response = self.clientAdmin.get(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 200)

    def test_get_list_customer(self):
        response = self.clientCustomer.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_get_detail_customer(self):
        response = self.clientCustomer.get(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 200)

    def test_get_list_vendor(self):
        response = self.clientVendor.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_get_detail_vendor(self):
        response = self.clientVendor.get(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 200)

    def test_creation_vendor(self):
        assert self.clientVendor.id == self.data["added_by"]
        response = self.clientVendor.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_creation_validation(self):
        dish = Dish.objects.get(pk=self.dish.id)
        self.assertEqual(
            self.data,
            {"title": dish.title, "price": float(dish.price), "added_by": dish.added_by.id},
        )

    def test_creation_unauthorized(self):
        response = self.client.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 401)

    def test_creation_admin(self):
        response = self.clientAdmin.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_deletion_vendor(self):
        response = self.clientVendor.delete(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(bool(Dish.objects.filter(pk=self.dish.id)))

    def test_creation_customer(self):
        response = self.clientCustomer.post(self.base_url + str(self.dish.id) + "/")
        self.assertIn(response.status_code, [405, 403])

    def test_deletion_unauthorized(self):
        response = self.client.post(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 401)

    def test_deletion_admin(self):
        response = self.clientAdmin.post(self.base_url + str(self.dish.id) + "/")
        self.assertIn(response.status_code, [405, 403])

    def test_deletion_customer(self):
        response = self.clientCustomer.post(self.base_url + str(self.dish.id) + "/")
        self.assertIn(response.status_code, [405, 403])

    def test_add_for_other_user(self):
        new_vendor = VendorFactory()
        new_vendor.save()
        assert new_vendor.id != self.clientVendor.id, "This test require two different users."
        data = {
            "title": "test1",
            "price": 699,
            "added_by": new_vendor.id,
        }
        response = self.clientVendor.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 403)
