"""
URLs for the billing app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# aqui depois você registra os viewsets:
# router.register(r'billing', BillingViewSet, basename='billing')

urlpatterns = [
    path('', include(router.urls)),
]
