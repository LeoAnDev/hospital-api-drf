"""
Accounts app serializers.
"""

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model.
    """
    class Meta:
        """
        Meta class for GroupSerializer.
        """
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model
    """
    groups = GroupSerializer(many=True, read_only=True)
    """
    Serializer for the User model
    """
    class Meta:
        """
        Meta class for UserSerializer
        """
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'groups']
