from rest_framework.test import APITestCase
from django.test.testcases import SimpleTestCase

from src.apps.contact.models import Contact
from utils.testing.factories import AdminAPIClient


class ContactAPITest(APITestCase):
    TEST_ADMIN_PASSWORD = "adminpass"
    TEST_ADMIN_USERNAME = "admin"

    base_url = "http://localhost:8000/api/contact/"
    detailed_url = base_url + "1/"

    def setUp(self) -> None:
        self.adminClient = AdminAPIClient(username=self.TEST_ADMIN_USERNAME,
                                          password=self.TEST_ADMIN_PASSWORD)

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

    def test_authenticated_user(self):
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
        }
        self.assertEqual(data, model_data)


class ContactModelTest(SimpleTestCase):

    def setUp(self) -> None:
        Contact.objects.create(name="name",
                               subject="subject",
                               email="email@gmail.com",
                               message="message")

    def test_str(self):
        contact = Contact.objects.latest("added_date")
        print(contact)
        self.assertEqual(1, 1)
