import logging
import os

from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger("main")


def get_env_file():
    """
    Reads .env file, based on "ENV" environment variable.

    "ENV" var must be specified to successfully start app.
    """
    environment = os.environ.get("ENV")

    if environment is None:
        raise ImproperlyConfigured("'ENV' variable is missing. (DEV | PROD | TEST | DOCKER)")

    environment = environment.upper()

    file_name = None

    if environment == "DEV":
        file_name = "local.env"
    elif environment == "PROD":
        file_name = "prod.env"
    elif environment == "TEST":
        file_name = "test.env"
    elif environment == "DOCKER":
        file_name = "docker.env"

    if file_name is None:
        raise ImproperlyConfigured("Environment var isn't allowed.")

    return file_name


def setup_env_vars():
    """
    Wrapper function tries to export all defined env vars.
    If file doesn't exist throws exception.
    """
    filename = get_env_file()
    try:
        load_dotenv(filename)
    except FileNotFoundError:
        logger.warning("Not using .env file. Using manually set up vars.")
