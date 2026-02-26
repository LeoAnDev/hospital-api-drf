"""
Accounts app views
"""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer


# Custom permission class to allow access only to superusers
class IsSuperUser(permissions.BasePermission):
    """
    Permissão para permitir acesso apenas a superusers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the User model
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Group model
    """
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
