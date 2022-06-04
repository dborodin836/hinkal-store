from datetime import datetime as dt

from django.db import models


class Contact(models.Model):
    """Contains message from user from 'contact me' form"""

    name = models.CharField(max_length=255, verbose_name="Name")
    subject = models.CharField(max_length=255, verbose_name="Subject")
    email = models.EmailField(verbose_name="Sender")
    message = models.TextField(verbose_name="User's message")
    added_date = models.DateTimeField(default=dt.now)

    def __str__(self):
        return self.subject

    def __repr__(self):
        return f'Contact({self.name}, {self.subject}, {self.email}, {self.message}, {self.added_date})'
