from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates simple admin"

    def add_arguments(self, parser):
        ...

    def handle(self, *args, **options):
        User.objects.create_superuser("admin", "admin@example.com", "adminpass")
        self.stdout.write(
            """
Login: admin
Password: adminpass"""
        )
