from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.translation import gettext as _

# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(_("id"), editable=False, primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class DatetimeMixin:
    create_at = models.DateTimeField(_("Created at"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("Updated at"), auto_now=True, auto_now_add=False

# Create your models here.
