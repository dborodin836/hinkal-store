from django.db import models

from src.apps.core.models import TimeStampedModelMixin


class Contact(TimeStampedModelMixin):
    """Contains message from user from 'contact me' form"""

    name = models.CharField(max_length=255, verbose_name="Name")
    subject = models.CharField(max_length=255, verbose_name="Subject")
    email = models.EmailField(verbose_name="Sender")
    message = models.TextField(verbose_name="User's message")

    def __str__(self):
        return f"Contact: {self.subject}"

    def __repr__(self):
        return (
            f"Contact({self.name}, {self.subject}, {self.email}, {self.message}, "
            f"{self.created_at})"
        )
