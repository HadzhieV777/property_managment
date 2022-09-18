from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.user.manager import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(db_index=True, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    phone_number = models.IntegerField(blank=True, max_length=35)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.email}"

