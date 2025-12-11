"""
Vistas (ViewSets) para la API de Mantenimiento Industrial
Implementan operaciones CRUD para cada entidad
"""
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from .serializers import (
    EmpresaSerializer, EquipoSerializer, TecnicoSerializer,
    PlanMantencionSerializer, OrdenTrabajoSerializer
)


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar Empresas.
    Proporciona operaciones CRUD completas:
    - list: GET /api/empresas/
    - create: POST /api/empresas/
    - retrieve: GET /api/empresas/{id}/
    - update: PUT /api/empresas/{id}/
    - partial_update: PATCH /api/empresas/{id}/
    - destroy: DELETE /api/empresas/{id}/
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class EquipoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar Equipos.
    Proporciona operaciones CRUD completas con filtrado por empresa.
    """
    queryset = Equipo.objects.select_related('empresa').all()
    serializer_class = EquipoSerializer
    
    def get_queryset(self):
        """
        Permite filtrar equipos por empresa usando query parameter.
        Ejemplo: /api/equipos/?empresa=1
        """
        queryset = super().get_queryset()
        empresa_id = self.request.query_params.get('empresa', None)
        if empresa_id is not None:
            queryset = queryset.filter(empresa_id=empresa_id)
        return queryset


class TecnicoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar Técnicos.
    Proporciona operaciones CRUD completas.
    """
    queryset = Tecnico.objects.select_related('usuario').all()
    serializer_class = TecnicoSerializer


class PlanMantencionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar Planes de Mantención.
    Proporciona operaciones CRUD completas con filtrado.
    """
    queryset = PlanMantencion.objects.select_related('equipo', 'equipo__empresa').all()
    serializer_class = PlanMantencionSerializer
    
    def get_queryset(self):
        """
        Permite filtrar planes por equipo o estado activo.
        Ejemplos:
        - /api/planes-mantencion/?equipo=1
        - /api/planes-mantencion/?activo=true
        """
        queryset = super().get_queryset()
        equipo_id = self.request.query_params.get('equipo', None)
        activo = self.request.query_params.get('activo', None)
        
        if equipo_id is not None:
            queryset = queryset.filter(equipo_id=equipo_id)
        if activo is not None:
            queryset = queryset.filter(activo=activo.lower() == 'true')
        
        return queryset


class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar Órdenes de Trabajo.
    Proporciona operaciones CRUD completas con filtrado avanzado.
    """
    queryset = OrdenTrabajo.objects.select_related(
        'plan', 'equipo', 'tecnico'
    ).all()
    serializer_class = OrdenTrabajoSerializer
    
    def get_queryset(self):
        """
        Permite filtrar órdenes por estado, técnico o equipo.
        Ejemplos:
        - /api/ordenes-trabajo/?estado=pendiente
        - /api/ordenes-trabajo/?tecnico=1
        - /api/ordenes-trabajo/?equipo=1
        """
        queryset = super().get_queryset()
        estado = self.request.query_params.get('estado', None)
        tecnico_id = self.request.query_params.get('tecnico', None)
        equipo_id = self.request.query_params.get('equipo', None)
        
        if estado is not None:
            queryset = queryset.filter(estado=estado)
        if tecnico_id is not None:
            queryset = queryset.filter(tecnico_id=tecnico_id)
        if equipo_id is not None:
            queryset = queryset.filter(equipo_id=equipo_id)
        
        return queryset


@api_view(['GET'])
@permission_classes([AllowAny])
def api_estado(request):
    """
    Endpoint de estado para verificar la disponibilidad de la API.
    
    GET /api/estado/
    
    Retorna información sobre el estado de la API en formato JSON.
    No requiere autenticación.
    """
    return Response({
        'estado': 'operativa',
        'mensaje': 'API de Mantenimiento Industrial funcionando correctamente',
        'version': '1.0.0',
        'endpoints': {
            'empresas': '/api/empresas/',
            'equipos': '/api/equipos/',
            'tecnicos': '/api/tecnicos/',
            'planes_mantencion': '/api/planes-mantencion/',
            'ordenes_trabajo': '/api/ordenes-trabajo/',
            'autenticacion': '/api/auth/login/',
        }
    }, status=status.HTTP_200_OK)
