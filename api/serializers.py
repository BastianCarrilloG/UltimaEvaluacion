"""
Serializers para la API de Mantenimiento Industrial
Convierten los modelos Django a formato JSON y viceversa
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo


class EmpresaSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Empresa.
    Convierte objetos Empresa a JSON y valida datos de entrada.
    """
    class Meta:
        model = Empresa
        fields = ['id', 'nombre', 'direccion', 'rut', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']


class EquipoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Equipo.
    Incluye información anidada de la empresa.
    """
    empresa_nombre = serializers.CharField(source='empresa.nombre', read_only=True)
    
    class Meta:
        model = Equipo
        fields = [
            'id', 'empresa', 'empresa_nombre', 'nombre', 
            'numero_serie', 'critico', 'fecha_instalacion'
        ]
        read_only_fields = ['id']


class TecnicoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Técnico.
    Incluye información del usuario asociado.
    """
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Tecnico
        fields = [
            'id', 'usuario', 'usuario_username', 
            'nombre_completo', 'especialidad', 'telefono'
        ]
        read_only_fields = ['id']


class PlanMantencionSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Plan de Mantención.
    Incluye información del equipo asociado.
    """
    equipo_nombre = serializers.CharField(source='equipo.nombre', read_only=True)
    empresa_nombre = serializers.CharField(source='equipo.empresa.nombre', read_only=True)
    
    class Meta:
        model = PlanMantencion
        fields = [
            'id', 'equipo', 'equipo_nombre', 'empresa_nombre',
            'nombre', 'frecuencia_dias', 'activo'
        ]
        read_only_fields = ['id']


class OrdenTrabajoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Orden de Trabajo.
    Incluye información anidada de plan, equipo y técnico.
    """
    plan_nombre = serializers.CharField(source='plan.nombre', read_only=True)
    equipo_nombre = serializers.CharField(source='equipo.nombre', read_only=True)
    tecnico_nombre = serializers.CharField(source='tecnico.nombre_completo', read_only=True)
    
    class Meta:
        model = OrdenTrabajo
        fields = [
            'id', 'plan', 'plan_nombre', 'equipo', 'equipo_nombre',
            'tecnico', 'tecnico_nombre', 'estado', 'fecha_programada',
            'fecha_completada', 'notas'
        ]
        read_only_fields = ['id', 'fecha_completada']
    
    def validate(self, data):
        """
        Validación personalizada para asegurar que el equipo coincida con el plan.
        """
        if 'plan' in data and 'equipo' in data:
            if data['plan'].equipo != data['equipo']:
                raise serializers.ValidationError(
                    "El equipo seleccionado no coincide con el equipo del plan de mantención"
                )
        return data
