from django.contrib import admin
from .models import AppUser


@admin.register(AppUser)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'first_name', 'last_name')

