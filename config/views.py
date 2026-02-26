"""
Global views configuration for the project
"""

from django.http import JsonResponse
from django.views import View


class ApiRootView(View):
    """
    Root view for the API
    """

    def get(self, request):
        """
        Handle GET requests to the API root endpoint.
        """
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        return JsonResponse({
            "message": "Bem-vindo à API do Projeto Taynah Amaral",
            "version": "1.0",
            "auth": "/api/token/",
            "docs": "api/docs/",
            "user_agent": user_agent
        })
