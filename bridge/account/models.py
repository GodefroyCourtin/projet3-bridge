from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class My_user(AbstractUser):
    """Contain user information."""
    administrateur = models.BooleanField(default=False)