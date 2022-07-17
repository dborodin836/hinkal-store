import io
from contextlib import redirect_stdout

from django.core.management import call_command
from rest_framework.test import APITestCase

from src.apps.contact.models import Contact
from src.apps.core.testing.api_clients import AdminAPIClient


class ContactAPITest(APITestCase):
    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    base_url = "http://localhost:8000/api/contact/"
    detailed_url = base_url + "1/"

    @classmethod
    def setUpTestData(cls) -> None:
        with redirect_stdout(io.StringIO()):
            call_command("loaddata", "fixtures/groups.json", app_label="auth")
        cls.adminClient = AdminAPIClient(  # type: ignore
            username=cls.TEST_ADMIN_USERNAME, password=cls.TEST_ADMIN_PASSWORD
        )

    def test_unauthenticated_user(self):
        """
        Checks all unauthenticated user's methods.
        """

        # GET
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 401)

        response = self.client.get(self.detailed_url)
        self.assertEqual(response.status_code, 401)

        # POST

        data = {
            "name": "name",
            "subject": "subject",
            "email": "email@gmail.com",
            "message": "message",
        }
        self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 401)

        # DELETE
        response = self.client.delete(self.base_url)
        self.assertEqual(response.status_code, 401)

    def test_admin_user(self):
        """
        Checks all authenticated user's methods.
        """
        # GET
        response = self.adminClient.get(self.base_url)
        self.assertEqual(response.status_code, 200)

        response = self.adminClient.get(self.detailed_url)
        self.assertEqual(response.status_code, 404)

        # POST

        data = {
            "name": "name",
            "subject": "subject",
            "email": "email@gmail.com",
            "message": "message",
            "created_at": "2015-05-16T05:50:06",
        }
        response = self.adminClient.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 201)

        # Data validation
        contact = Contact.objects.latest("created_at")
        model_data = {
            "name": contact.name,
            "subject": contact.subject,
            "email": contact.email,
            "message": contact.message,
            "created_at": "2015-05-16T05:50:06",
        }
        self.assertEqual(data, model_data)

        # DELETE
        response = self.adminClient.delete(self.detailed_url)
        self.assertEqual(response.status_code, 405)

        # PATCH
        response = self.adminClient.patch(self.detailed_url)
        self.assertEqual(response.status_code, 405)

        # PUT
        response = self.adminClient.patch(self.detailed_url)
        self.assertEqual(response.status_code, 405)
