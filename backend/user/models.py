from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Countries(models.Model):
    """Table for countries and their codes"""
    fullname = models.CharField(max_length=100)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.fullname


class UserAddress(models.Model):
    """Contains user's addresses"""
    user_id = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50)
    postal_code = models.PositiveIntegerField()
    county = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)
    telephone = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)

    def __str__(self):
        return self.user_id.username


class CustomUser(AbstractUser):
    """Custom user model with some extra fields"""
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', default=settings.DEFAULT_USER_PHOTO)
    is_vendor = models.BooleanField(default=False)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
