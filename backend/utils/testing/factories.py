from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import logging

logger = logging.getLogger('main')


class AdminAPIClient(APIClient):
    """
    APIClient that represents superuser/admin client.
    """

    def __init__(self, username: str, password: str,  enforce_csrf_checks=False, **defaults):
        super(AdminAPIClient, self).__init__(enforce_csrf_checks=False, **defaults)
        logger.info("AdminAPIClient is being constructed.")
        self.__username = username
        self.__password = password
        self._setup_admin_client()
        self.credentials()

    def __create_test_superuser(self) -> None:
        """
        Creates superuser.
        """
        self._admin_user = User.objects.create(
            username=self.__username,
            is_superuser=True,
            is_staff=True
        )
        logger.debug("User created")
        self._admin_user.set_password(self.__password)
        logger.debug("Password set")
        self._admin_user.save()

    def __obtain_token_for_admin_client(self) -> None:
        """
        Obtains Auth token for the adminAPIClient.
        """
        self.adminClient = APIClient()
        logger.debug('Client created')

        credentials = {"password": self.__username, "username": self.__password}
        self.adminClient.post("http://localhost:8000/auth/token/login/", credentials)

        try:
            self.__token = Token.objects.get(user=self._admin_user).key
            logger.debug("Token is %s" % self.__token)
        except Token.DoesNotExist:
            logger.error("Token doest not exist...")
            raise Exception
        self.adminClient.credentials(HTTP_AUTHORIZATION=f'Token {self.__token}')

    def _setup_admin_client(self):
        """
        Creates adminClient w/ token auth.
        """
        self.__create_test_superuser()
        self.__obtain_token_for_admin_client()
