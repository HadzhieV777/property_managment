from django.contrib import admin
from .models import SingleProperty


@admin.register(SingleProperty)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'type', 'status', 'tenant', 'price')

