import string
import random
from datetime import datetime

import factory

from src.apps.user.models import Vendor


def get_name(x):
    return (
        "".join([random.choice(string.ascii_letters + "123456789_-") for _ in range(30)])
        + str(datetime.now())[:10]
    )


class VendorFactory(factory.Factory):
    """
    Creates a new ``Vendor`` object.
    Username will be a random 30 character value.
    Email will be ``{username}@example.com``.
    Password will be ``testpass`` by default.
    """

    username = factory.LazyAttribute(get_name)
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
