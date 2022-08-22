from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from psycopg2 import IntegrityError as PsycopgIntegrityError


class Command(BaseCommand):
    help = "Creates simple admin"

    def add_arguments(self, parser):
        ...

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser("admin", "admin@example.com", "adminpass")
        except (IntegrityError, PsycopgIntegrityError):
            self.stdout.write("Sample superuser already exists. Skipping...")
        else:
            self.stdout.write("Login: admin\nPassword: adminpass")
