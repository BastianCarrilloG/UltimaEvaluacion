"""
URLs de la API de Mantenimiento Industrial
Define los endpoints para cada recurso
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    EmpresaViewSet, EquipoViewSet, TecnicoViewSet,
    PlanMantencionViewSet, OrdenTrabajoViewSet, api_estado
)

# Router para registrar los ViewSets automáticamente
router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet, basename='empresa')
router.register(r'equipos', EquipoViewSet, basename='equipo')
router.register(r'tecnicos', TecnicoViewSet, basename='tecnico')
router.register(r'planes-mantencion', PlanMantencionViewSet, basename='plan-mantencion')
router.register(r'ordenes-trabajo', OrdenTrabajoViewSet, basename='orden-trabajo')

urlpatterns = [
    # Endpoint de estado de la API
    path('estado/', api_estado, name='api-estado'),
    
    # Endpoint de autenticación (login para obtener token)
    path('auth/login/', obtain_auth_token, name='api-login'),
    
    # Incluir todas las rutas del router
    path('', include(router.urls)),
]
