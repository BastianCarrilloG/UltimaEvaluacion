"""
Configuración del panel de administración de Django
"""
from django.contrib import admin
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'direccion', 'fecha_creacion')
    search_fields = ('nombre', 'rut')
    list_filter = ('fecha_creacion',)
    readonly_fields = ('fecha_creacion',)


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_serie', 'empresa', 'critico', 'fecha_instalacion')
    search_fields = ('nombre', 'numero_serie', 'empresa__nombre')
    list_filter = ('critico', 'fecha_instalacion', 'empresa')
    autocomplete_fields = ['empresa']


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'especialidad', 'telefono', 'usuario')
    search_fields = ('nombre_completo', 'especialidad', 'usuario__username')
    list_filter = ('especialidad',)


@admin.register(PlanMantencion)
class PlanMantencionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'equipo', 'frecuencia_dias', 'activo')
    search_fields = ('nombre', 'equipo__nombre')
    list_filter = ('activo', 'equipo__empresa')
    autocomplete_fields = ['equipo']


@admin.register(OrdenTrabajo)
class OrdenTrabajoAdmin(admin.ModelAdmin):
    list_display = ('id', 'equipo', 'tecnico', 'estado', 'fecha_programada', 'fecha_completada')
    search_fields = ('equipo__nombre', 'tecnico__nombre_completo', 'notas')
    list_filter = ('estado', 'fecha_programada', 'equipo__empresa')
    autocomplete_fields = ['plan', 'equipo', 'tecnico']
    readonly_fields = ('fecha_completada',)
    
    fieldsets = (
        ('Información General', {
            'fields': ('plan', 'equipo', 'tecnico', 'estado')
        }),
        ('Fechas', {
            'fields': ('fecha_programada', 'fecha_completada')
        }),
        ('Detalles', {
            'fields': ('notas',)
        }),
    )
