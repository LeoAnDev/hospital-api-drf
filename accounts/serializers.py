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
        fields = [
            'id', 'username', 'email', 'is_active',
            'first_name', 'last_name', 'groups', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        """
        Validate that the username is uppercase.
        """
        return value.upper()

    def validate_first_name(self, value):
        """
        Validate that the first name is uppercase.
        """
        return value.upper()

    def validate_last_name(self, value):
        """
        Validate that the last name is uppercase.
        """
        return value.upper()

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', [])
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        if groups:
            user.groups.set(groups)
        return user

    def update(self, instance, validated_data):
        for attr in ['username', 'first_name', 'last_name']:
            if attr in validated_data:
                setattr(instance, attr, validated_data[attr].upper())
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        if groups is not None:
            instance.groups.set(groups)
        return instance
