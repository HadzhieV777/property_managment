from rest_framework import exceptions
from rest_framework.permissions import BasePermission, IsAuthenticated
from django.utils.translation import gettext_lazy as _

from core.user.models import AppUser

# TODO TEST AUTHORIZATION ISSUE FUNCTIONALITY

"""
Handle Authorization issue  using a custom 
permission checker instead of using django rest framework's default
"""
class AllowOptionsAuthentication(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return request.user and request.user.is_authenticated


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, AppUser):
            return request.user == obj
        raise exceptions.PermissionDenied(detail=_("Received object of wrong instance"), code=403)