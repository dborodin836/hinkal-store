from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import logging

from src.apps.user.models import Customer, Vendor

logger = logging.getLogger("debug")


class BaseUserAPIClient(APIClient):
    def __init__(self, username: str, password: str, enforce_csrf_checks=False, **defaults):
        super().__init__(enforce_csrf_checks, **defaults)
        self.username = username
        self.password = password

        self.setup_admin_client()

    def setup_admin_client(self):
        """
        Creates adminClient w/ token auth.
        """
        self.create_user()
        self.obtain_token_for_user()

    def obtain_token_for_user(self) -> None:
        """
        Obtains Auth token for the adminAPIClient.
        """

        credentials = {"password": self.password, "username": self.username}
        APIClient().post("http://localhost:8000/auth/token/login/", credentials)

        try:
            self.__token = Token.objects.get(user_id=self.id).key
        except Token.DoesNotExist:
            logger.error("Token doest not exist...")
            logger.info("All tokens : %s" % Token.objects.all())
            raise Token.DoesNotExist

        self.credentials(HTTP_AUTHORIZATION=f"Token {self.__token}")

    @property
    def user(self):
        return self._user

    @property
    def id(self):
        return self._user.id


class AdminAPIClient(BaseUserAPIClient):
    """
    APIClient that represents superuser/admin client.
    """

    def create_user(self) -> None:
        """
        Creates regular user.
        """
        self._user = User.objects.create(username=self.username, is_superuser=True, is_staff=True)
        self._user.set_password(self.password)
        self._user.save()


class CustomerAPIClient(BaseUserAPIClient):
    """
    APIClient that represents customer client.
    """

    def create_user(self) -> None:
        """
        Creates regular user.
        """
        self._user = Customer.objects.create(username=self.username)
        self._user.set_password(self.password)
        self._user.save()


class VendorAPIClient(BaseUserAPIClient):
    """
    APIClient that represents vendor client.
    """

    def create_user(self) -> None:
        """
        Creates regular user.
        """
        self._user = Vendor.objects.create(username=self.username)
        self._user.set_password(self.password)
        self._user.save()
