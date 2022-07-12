from rest_framework.test import APITestCase

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

    def setUp(self) -> None:
        self.vendor = VendorFactory().save()
        self.clientAdmin = AdminAPIClient(
            username=self.TEST_ADMIN_USERNAME, password=self.TEST_ADMIN_PASSWORD
        )
        self.clientVendor = VendorAPIClient(
            username=self.TEST_VENDOR_USERNAME, password=self.TEST_VENDOR_PASSWORD
        )
        self.clientCustomer = CustomerAPIClient(
            username=self.TEST_CUSTOMER_USERNAME, password=self.TEST_CUSTOMER_PASSWORD
        )
        category = Category.objects.create(name="Dish")

        self.data = {
            "title": "test1",
            "price": 699,
            "added_by": 2,
        }

        self.dish = Dish.objects.create(
            title="test1", description="", price=699, category=category, added_by=self.vendor
        )

        self.data_update = {
            "title": "test1update",
            "price": 899,
            "added_by": 2,
        }

    def test_get_list(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_get_detail(self):
        response = self.client.get(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 200)

    def test_creation_vendor(self):
        response = self.clientVendor.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 201)

    def test_creation_validation(self):
        dish = Dish.objects.get(pk=self.dish.id)
        self.assertEqual(
            self.data, {"title": dish.title, "price": float(dish.price), "added_by": 2}
        )

    def test_creation_unauthorized(self):
        response = self.client.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 401)

    def test_creation_admin(self):
        response = self.clientAdmin.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 403)

    def test_deletion_vendor(self):
        response = self.clientVendor.delete(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(bool(Dish.objects.filter(pk=self.dish.id)))

    def test_creation_customer(self):
        response = self.clientCustomer.post(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 403)

    def test_deletion_unauthorized(self):
        response = self.client.post(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 401)

    def test_deletion_admin(self):
        response = self.clientAdmin.post(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 403)

    def test_deletion_customer(self):
        response = self.clientCustomer.post(self.base_url + str(self.dish.id) + "/")
        self.assertEqual(response.status_code, 403)
