"""
URLs for the customers app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# aqui depois você registra os viewsets:
# router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]
