from django.db import models
from django.contrib.auth.models import User

from datetime import datetime as dt


class Dish(models.Model):
    """Contains dishes"""
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')
    added_date = models.DateTimeField(default=dt.now(), verbose_name='Added')
    added_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Vendor')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
