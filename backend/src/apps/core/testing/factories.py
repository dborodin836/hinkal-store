import string
import random
from datetime import datetime

import factory

from src.apps.user.models import Vendor


class VendorFactory(factory.Factory):
    """
    Creates a new ``Vendor`` object.
    Username will be a random 30 character value concatenated with today's date.
    Email will be ``{username}@example.com``.
    Password will be ``testpass`` by default.
    """

    @factory.lazy_attribute
    def username(self):
        """
        Returns random name.
        """
        return (
            "".join([random.choice(string.ascii_letters + "123456789_-") for _ in range(30)])
            + str(datetime.now())[:10]
        )

    email = f"{username}@example.com"
    password = factory.PostGenerationMethodCall("set_password", "testpass")
    is_active = True

    class Meta:
        model = Vendor


class CustomerFactory(VendorFactory):
    """
    Creates a new ``Customer`` object.
    Username will be a random 30 character value.
    Email will be ``{username}@example.com``.
    Password will be ``testpass`` by default.
    """

    class Meta:
        model = Vendor
