from django.core.management import call_command
from rest_framework.test import APITestCase

from src.apps.core.decorators import hide_stdout
from src.apps.core.testing.api_clients import AdminAPIClient
from src.apps.user.models import Customer, Vendor


class CustomerAPITest(APITestCase):
    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    base_url = "http://localhost:8000/api/customers/"
    detailed_url = base_url + "1/"

    @classmethod
    @hide_stdout
    def setUpTestData(cls) -> None:
        call_command("loaddata", "fixtures/groups.json", app_label="auth")
        cls.adminClient = AdminAPIClient(  # type: ignore
            username=cls.TEST_ADMIN_USERNAME, password=cls.TEST_ADMIN_PASSWORD
        )

    def test_create_customer(self):
        user_data = {"username": "testusername", "password": "sometestpassword"}
        response = self.client.post(self.base_url, data=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Customer.objects.filter(username=user_data["username"]).exists())


class VendorAPITest(APITestCase):
    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    base_url = "http://localhost:8000/api/vendors/"
    detailed_url = base_url + "1/"

    @classmethod
    @hide_stdout
    def setUpTestData(cls) -> None:
        call_command("loaddata", "fixtures/groups.json", app_label="auth")
        cls.adminClient = AdminAPIClient(  # type: ignore
            username=cls.TEST_ADMIN_USERNAME, password=cls.TEST_ADMIN_PASSWORD
        )

    def test_create_customer(self):
        user_data = {"username": "testusername", "password": "sometestpassword"}
        response = self.client.post(self.base_url, data=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Vendor.objects.filter(username=user_data["username"]).exists())
