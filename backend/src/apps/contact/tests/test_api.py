from rest_framework.test import APITestCase

from src.apps.contact.models import Contact
from utils.testing.factories import AdminAPIClient


class ContactAPITest(APITestCase):
    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    base_url = "http://localhost:8000/api/contact/"
    detailed_url = base_url + "1/"

    def setUp(self) -> None:
        self.adminClient = AdminAPIClient(
            username=self.TEST_ADMIN_USERNAME, password=self.TEST_ADMIN_PASSWORD
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
            "added_date": "2015-05-16T05:50:06",
        }
        response = self.adminClient.post(self.base_url, data=data)
        self.assertEqual(response.status_code, 201)

        # Data validation
        contact = Contact.objects.latest("added_date")
        model_data = {
            "name": contact.name,
            "subject": contact.subject,
            "email": contact.email,
            "message": contact.message,
            "added_date": "2015-05-16T05:50:06",
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
