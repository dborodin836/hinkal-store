import datetime
import pytz
from django.test.testcases import TestCase

from src.apps.contact.models import Contact


class ContactModelTest(TestCase):
    def setUp(self) -> None:
        Contact.objects.create(
            name="name",
            subject="subject",
            email="email@gmail.com",
            message="message",
            created_at=datetime.datetime(1, 1, 1, 1, 1, tzinfo=pytz.UTC),
        )

    def test_str(self):
        """
        Testing __str__ method.
        """
        contact = Contact.objects.latest("created_at")
        self.assertEqual(str(contact), "Contact: subject")
