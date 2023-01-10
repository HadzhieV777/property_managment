from django.contrib import admin
from .models import SingleProperty


@admin.register(SingleProperty)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'baths', 'bedrooms', 'city', 'maintenance', 'owner', 'price', 'rented', 'type', 'zip')     

