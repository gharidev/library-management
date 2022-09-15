"""
Permissions for the API views of core app.
"""

from rest_framework.permissions import BasePermission
from django.conf import settings

from core.models import User

class IsAdminOnly(BasePermission):
    """
    Allows access only to authenticated admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.type == User.Types.ADMIN)