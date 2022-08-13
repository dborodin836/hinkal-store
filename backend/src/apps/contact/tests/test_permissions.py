from django.core.management import call_command
from rest_framework.test import APITestCase

from src.apps.core.decorators import hide_stdout
from src.apps.core.testing.api_clients import AdminAPIClient, VendorAPIClient, CustomerAPIClient


class ContactPermissionTest(APITestCase):
    TEST_CUSTOMER_PASSWORD = "customer"
    TEST_CUSTOMER_USERNAME = "customerpass"

    TEST_VENDOR_PASSWORD = "vendor"
    TEST_VENDOR_USERNAME = "vendorpass"

    TEST_ADMIN_PASSWORD = "admin"
    TEST_ADMIN_USERNAME = "adminpass"

    base_url = "http://localhost:8000/api/contact/"
    detailed_url = base_url + "1/"

    @classmethod
    @hide_stdout
    def setUpTestData(cls) -> None:
        call_command("loaddata", "fixtures/groups.json", app_label="auth")
        cls.customerClient = CustomerAPIClient(  # type: ignore
            username=cls.TEST_CUSTOMER_USERNAME, password=cls.TEST_CUSTOMER_PASSWORD
        )
        cls.vendorClient = VendorAPIClient(  # type: ignore
            username=cls.TEST_VENDOR_USERNAME, password=cls.TEST_VENDOR_PASSWORD
        )
        cls.adminClient = AdminAPIClient(  # type: ignore
            username=cls.TEST_ADMIN_USERNAME, password=cls.TEST_ADMIN_PASSWORD
        )

    def test_unauthenticated_get_api(self):
        response = self.client.get(self.base_url)
        self.assertIn(response.status_code, [403, 401])

    def test_customer_get_api(self):
        response = self.customerClient.get(self.base_url)
        self.assertIn(response.status_code, [403, 401])

    def test_vendor_get_api(self):
        response = self.vendorClient.get(self.base_url)
        self.assertIn(response.status_code, [403, 401])

    def test_admin_get_api(self):
        response = self.adminClient.get(self.base_url)
        self.assertEqual(response.status_code, 200)
