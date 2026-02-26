"""
URLs for the catalog app
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# aqui depois você registra os viewsets:
# router.register(r'catalog', CatalogViewSet, basename='catalog')

urlpatterns = [
    path('', include(router.urls)),
]
