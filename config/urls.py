"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

# Import the include function to include URLs from other apps
from django.urls import include, path

# Import Swagger/OpenAPI schema view for API documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Import views for JWT authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Import the API root view
from .views import ApiRootView

# Create the schema view for Swagger and Redoc documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Taynah Amaral API",
        default_version="v1",
        description="Documentação Swagger e Redoc da API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', ApiRootView.as_view()),
    path('admin/', admin.site.urls),

    # Include URLs from JWT authentication
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    # Refresh token endpoint
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    # Include URLs from custom apps
    path('api/accounts/', include('accounts.urls'), name='accounts'),
    path('api/customers/', include('customers.urls'), name='customers'),
    path('api/catalog/', include('catalog.urls'), name='catalog'),
    path('api/orders/', include('orders.urls'), name='orders'),
    path('api/billing/', include('billing.urls'), name='billing'),
    path('api/delivery/', include('delivery.urls'), name='delivery'),

    # Swagger and Redoc documentation endpoints
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='swagger-ui'),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='redoc-ui'
    ),
]
