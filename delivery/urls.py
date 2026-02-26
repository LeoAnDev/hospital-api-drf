"""
URLs for the delivery app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# aqui depois você registra os viewsets:
# router.register(r'delivery', DeliveryViewSet, basename='delivery')

urlpatterns = [
    path('', include(router.urls)),
]
