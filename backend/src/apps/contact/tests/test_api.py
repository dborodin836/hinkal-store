from rest_framework.test import APITestCase
from utils.testing.factories import AdminAPIClient


class ContactAPITest(APITestCase):

    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    def setUp(self) -> None:
        self.adminClient = AdminAPIClient(username=self.TEST_ADMIN_USERNAME,
                                          password=self.TEST_ADMIN_PASSWORD)

    def test_get_contact_returns_correct_status_code_without_credentials(self):
        """
        Checks if user can't access page w/o credentials.
        """
        url = "http://localhost:8000/api/contact/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_get_contact_returns_correct_status_code_with_credentials(self):
        """
        Checks if user can access page w/ auth token.
        """
        url = "http://localhost:8000/api/contact/"
        response = self.adminClient.get(url)
        self.assertEqual(response.status_code, 200)
