"""
URLs for the accounts app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# aqui depois você registra os viewsets:
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
