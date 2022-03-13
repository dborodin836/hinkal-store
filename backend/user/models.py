from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', default=settings.DEFAULT_USER_PHOTO)
    is_vendor = models.BooleanField(default=False)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
