from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class TimeStampedModelMixin(models.Model):
    """
    Abstract model mixin to time stamp instances creation and update.

    Adds 2 models fields "created_at" and "updated_at".
    """

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        abstract = True


class AddedByModelMixin(models.Model):
    """
    Abstract model mixin to add user to instances.

    Adds one field "added_by". By default, connects to the default
    django "User" model.
    """

    added_by = models.ForeignKey(User, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class TimeStampedAddedByModel(TimeStampedModelMixin, AddedByModelMixin):
    """
    Combines functionality of AddedByModelMixin and TimeStampedModelMixin.
    """

    class Meta:
        abstract = True
