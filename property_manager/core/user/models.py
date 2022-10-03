from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from core.user.manager import AppUserManager


class AppUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(db_index=True, unique=True)
    phone_number = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    objects = AppUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    def __str__(self):
        return f"{self.email}"

