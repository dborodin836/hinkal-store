#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


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


def main():
    """Run administrative tasks."""
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
    get_envs_from_file('local.env')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
