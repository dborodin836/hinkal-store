from contextlib import redirect_stdout
import io

from django.core.management import call_command
from django.test import TestCase

from src.apps.core.testing.api_clients import CustomerAPIClient, AdminAPIClient, VendorAPIClient


class CustomerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        with redirect_stdout(io.StringIO()):
            call_command("loaddata", "fixtures/groups.json", app_label="auth")

    def setUp(self) -> None:
        self.client: CustomerAPIClient = CustomerAPIClient(username="test1", password="test_pass")

    def test_customer_rights(self):
        self.assertFalse(self.client.user.is_superuser)


class VendorTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        with redirect_stdout(io.StringIO()):
            call_command("loaddata", "fixtures/groups.json", app_label="auth")

    def setUp(self) -> None:
        self.client: VendorAPIClient = VendorAPIClient(username="test1", password="test_pass")

    def test_customer_rights(self):
        self.assertFalse(self.client.user.is_superuser)


class AdminTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        with redirect_stdout(io.StringIO()):
            call_command("loaddata", "fixtures/groups.json", app_label="auth")

    def setUp(self) -> None:
        self.client: AdminAPIClient = AdminAPIClient(username="test1", password="test_pass")

    def test_customer_rights(self):
        self.assertTrue(self.client.user.is_superuser)
