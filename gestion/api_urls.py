# gestion/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ClienteViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)  # Registra el ViewSet

urlpatterns = [
    path('', include(router.urls)),  # Incluye las URLs de la API
]