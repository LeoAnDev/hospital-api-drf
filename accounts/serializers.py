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
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False)
    groups = GroupSerializer(many=True, read_only=True)

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

    def validate_first_name(self, value):
        """
        Validate the first_name field to uppercase
        """
        return value.upper()

    def validate_last_name(self, value):
        """
        Validate the last_name field to uppercase
        """
        return value.upper()

    def validate(self, attrs):
        request = self.context.get('request')
        if request and request.method in ['POST', 'PUT', 'PATCH']:
            groups_ids = request.data.get('groups')
            if not groups_ids:
                raise serializers.ValidationError(
                    {"groups": "O campo 'groups' não pode ser vazio."})
        return attrs

    def create(self, validated_data):
        groups_ids = self.context['request'].data.get('groups', [])
        user = User.objects.create_user(**validated_data)
        user.groups.set(groups_ids)
        return user

    def update(self, instance, validated_data):
        groups_ids = self.context['request'].data.get('groups', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if groups_ids is not None:
            instance.groups.set(groups_ids)
        return instance
