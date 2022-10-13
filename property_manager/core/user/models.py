from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from core.user.manager import AppUserManager


class AppUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    phone_number = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=70, blank=True)
    
    objects = AppUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

