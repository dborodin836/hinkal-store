from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient


class ContactAPITest(APITestCase):

    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    def _create_test_superuser(self) -> None:
        """
        Creates superuser.
        """
        self.admin = User.objects.create(
            username=self.TEST_ADMIN_USERNAME,
            is_superuser=True,
            is_staff=True
        )
        self.admin.set_password(self.TEST_ADMIN_PASSWORD)
        self.admin.save()

    def _obtain_token_for_admin_client(self) -> None:
        """
        Obtains Auth token for the adminAPIClient.
        """
        self.adminClient = APIClient()

        credentials = {"password": self.TEST_ADMIN_PASSWORD, "username": self.TEST_ADMIN_USERNAME}
        self.adminClient.post("http://localhost:8000/auth/token/login/", credentials)

        self.token = Token.objects.get(user=self.admin).key
        self.adminClient.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def _setup_admin_client(self):
        """
        Creates adminClient w/ token auth.
        """
        self._create_test_superuser()
        self._obtain_token_for_admin_client()

    def setUp(self) -> None:
        self._setup_admin_client()

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
