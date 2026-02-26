"""
Tests for the accounts app.
"""

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountsAPITest(APITestCase):
    """
    Test cases for the accounts API endpoints.
    """
    def setUp(self):
        self.group = Group.objects.create(name="TestGroup")
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
            is_staff=True
        )
        self.user.groups.add(self.group)
        # Obtain JWT token for authentication
        response = self.client.post(
            reverse('token_obtain_pair'),
            {'username': 'testuser', 'password': 'testpass123'},
            format='json'
        )
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_list_users(self):
        """
        Test listing users
        """
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Test creating a new user
        """
        url = reverse('user-list')
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpass123",
            "groups": [self.group.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_groups(self):
        """
        Test listing groups
        """
        url = reverse('group-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
