"""
Validadores personalizados para la API de Mantenimiento Industrial
"""
import re
from django.core.exceptions import ValidationError


def validar_rut_chileno(rut):
    """
    Valida el formato y dígito verificador de un RUT chileno.
    Formatos aceptados: 12.345.678-9 o 12345678-9
    """
    # Limpiar el RUT de puntos y guiones
    rut_limpio = rut.replace('.', '').replace('-', '').upper()
    
    # Verificar que tenga entre 8 y 9 caracteres
    if len(rut_limpio) < 8 or len(rut_limpio) > 9:
        raise ValidationError('El RUT debe tener entre 8 y 9 caracteres')
    
    # Separar número y dígito verificador
    numero = rut_limpio[:-1]
    dv = rut_limpio[-1]
    
    # Verificar que el número sea numérico
    if not numero.isdigit():
        raise ValidationError('El RUT debe contener solo números antes del dígito verificador')
    
    # Calcular dígito verificador
    suma = 0
    multiplicador = 2
    
    for digito in reversed(numero):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    resto = suma % 11
    dv_calculado = 11 - resto
    
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)
    
    # Comparar dígito verificador
    if dv != dv_calculado:
        raise ValidationError('El dígito verificador del RUT no es válido')


def validar_telefono_chileno(telefono):
    """
    Valida el formato de un teléfono chileno.
    Formatos aceptados:
    - +56912345678
    - +56 9 1234 5678
    - 912345678
    - 9 1234 5678
    """
    # Limpiar espacios
    telefono_limpio = telefono.replace(' ', '').replace('-', '')
    
    # Patrón para teléfono chileno
    # Acepta: +56912345678 o 912345678
    patron = r'^(\+?56)?9\d{8}$'
    
    if not re.match(patron, telefono_limpio):
        raise ValidationError(
            'El teléfono debe tener formato chileno válido. '
            'Ejemplos: +56912345678, 912345678'
        )


def validar_numero_serie(numero_serie):
    """
    Valida que el número de serie tenga un formato alfanumérico válido.
    Debe tener entre 5 y 50 caracteres.
    """
    if len(numero_serie) < 5 or len(numero_serie) > 50:
        raise ValidationError('El número de serie debe tener entre 5 y 50 caracteres')
    
    if not re.match(r'^[A-Za-z0-9\-_]+$', numero_serie):
        raise ValidationError(
            'El número de serie solo puede contener letras, números, guiones y guiones bajos'
        )
