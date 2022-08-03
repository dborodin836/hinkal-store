import logging
import os
import sys

from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger("main")


def get_envs_from_file(env_file="local.env") -> None:
    """
    Open file and set the all env variables it contains.

    Example:

    # "./local.env" #
        ...
        # DB settings        -- will be ignored
        DB_HOST=foobar       -- will be set as "DB_HOST" environment variable with value "foobar"
        DB_PASS=span_eggs       os.environ["DB_HOST"] = "foobar"
        ...
    """
    with open(os.path.join(sys.path[0], env_file)) as env_file:
        for line in env_file:
            if line.strip().startswith("#"):
                continue
            try:
                key, value = line.strip().split("=", 1)
                if isinstance(value, str):
                    os.environ[key] = value
            # In case some comments exist in file
            except ValueError:
                continue


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
        get_envs_from_file(filename)
    except FileNotFoundError:
        logger.warning("Not using .env file. Using manually set up vars.")
