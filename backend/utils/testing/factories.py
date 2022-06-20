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
        logger.debug("AdminAPIClient is being constructed.")
        self.__username = username
        self.__password = password

        self.__setup_admin_client()

    def __setup_admin_client(self):
        """
        Creates adminClient w/ token auth.
        """
        self.__create_test_superuser()
        self.__obtain_token_for_admin_client()

    def __create_test_superuser(self) -> None:
        """
        Creates superuser.
        """
        self._admin_user = User.objects.create(
            username=self.__username,
            is_superuser=True,
            is_staff=True
        )
        self._admin_user.set_password(self.__password)
        self._admin_user.save()
        logger.debug("User created")

    def __obtain_token_for_admin_client(self) -> None:
        """
        Obtains Auth token for the adminAPIClient.
        """

        self.__client = APIClient()

        credentials = {"password": self.__password, "username": self.__username}
        self.__client.post("http://localhost:8000/auth/token/login/", credentials)

        try:
            self.__token = Token.objects.get(user_id=self._admin_user.id).key
        except Token.DoesNotExist:
            logger.error("Token doest not exist...")
            logger.info("All tokens : %s" % Token.objects.all())
            raise Token.DoesNotExist

        self.credentials(HTTP_AUTHORIZATION=f'Token {self.__token}')
