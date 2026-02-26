"""
Accounts app views
"""

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the User model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Group model
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
