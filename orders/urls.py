"""
URLs for the orders app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# aqui depois você registra os viewsets:
# router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
