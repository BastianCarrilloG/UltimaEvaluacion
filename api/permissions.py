"""
Permisos personalizados para la API de Mantenimiento Industrial
"""
from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado que permite:
    - Usuarios no autenticados: Solo lectura (GET, HEAD, OPTIONS)
    - Usuarios autenticados: CRUD completo (GET, POST, PUT, PATCH, DELETE)
    """
    
    def has_permission(self, request, view):
        # Métodos seguros (lectura) permitidos para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Métodos de escritura solo para usuarios autenticados
        return request.user and request.user.is_authenticated
