"""
Modelos para la API de Mantenimiento Industrial
"""
from django.db import models
from django.contrib.auth.models import User
from .validators import validar_rut_chileno, validar_telefono_chileno, validar_numero_serie


class Empresa(models.Model):
    """
    Modelo para representar empresas clientes.
    """
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    direccion = models.CharField(max_length=500, verbose_name='Dirección')
    rut = models.CharField(
        max_length=12,
        unique=True,
        validators=[validar_rut_chileno],
        verbose_name='RUT',
        help_text='Formato: 12.345.678-9 o 12345678-9'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Equipo(models.Model):
    """
    Modelo para representar equipos de las empresas.
    """
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='equipos',
        verbose_name='Empresa'
    )
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Equipo')
    numero_serie = models.CharField(
        max_length=50,
        unique=True,
        validators=[validar_numero_serie],
        verbose_name='Número de Serie'
    )
    critico = models.BooleanField(default=False, verbose_name='¿Es Crítico?')
    fecha_instalacion = models.DateField(verbose_name='Fecha de Instalación')
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['empresa', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} - {self.numero_serie}"


class Tecnico(models.Model):
    """
    Modelo para representar técnicos de mantenimiento.
    """
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='tecnico',
        verbose_name='Usuario'
    )
    nombre_completo = models.CharField(max_length=255, verbose_name='Nombre Completo')
    especialidad = models.CharField(max_length=255, verbose_name='Especialidad')
    telefono = models.CharField(
        max_length=20,
        validators=[validar_telefono_chileno],
        verbose_name='Teléfono',
        help_text='Formato: +56912345678 o 912345678'
    )
    
    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['nombre_completo']
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.especialidad}"


class PlanMantencion(models.Model):
    """
    Modelo para representar planes de mantención.
    """
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        related_name='planes_mantencion',
        verbose_name='Equipo'
    )
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Plan')
    frecuencia_dias = models.PositiveIntegerField(
        verbose_name='Frecuencia (días)',
        help_text='Cada cuántos días se debe realizar la mantención'
    )
    activo = models.BooleanField(default=True, verbose_name='¿Está Activo?')
    
    class Meta:
        verbose_name = 'Plan de Mantención'
        verbose_name_plural = 'Planes de Mantención'
        ordering = ['equipo', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre} (cada {self.frecuencia_dias} días)"


class OrdenTrabajo(models.Model):
    """
    Modelo para representar órdenes de trabajo.
    """
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    plan = models.ForeignKey(
        PlanMantencion,
        on_delete=models.CASCADE,
        related_name='ordenes_trabajo',
        verbose_name='Plan de Mantención'
    )
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        related_name='ordenes_trabajo',
        verbose_name='Equipo'
    )
    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ordenes_trabajo',
        verbose_name='Técnico Asignado'
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente',
        verbose_name='Estado'
    )
    fecha_programada = models.DateField(verbose_name='Fecha Programada')
    fecha_completada = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Fecha de Completación'
    )
    notas = models.TextField(blank=True, verbose_name='Notas')
    
    class Meta:
        verbose_name = 'Orden de Trabajo'
        verbose_name_plural = 'Órdenes de Trabajo'
        ordering = ['-fecha_programada']
    
    def __str__(self):
        return f"OT-{self.id} - {self.equipo.nombre} ({self.estado})"
