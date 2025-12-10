# Base de Datos - Instrucciones

## Importar la Base de Datos

### Opción 1: Importar dump completo (para revisión del profesor)

```bash
# 1. Crear la base de datos en MySQL
mysql -u root -p
CREATE DATABASE mantenimiento_industrial CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit;

# 2. Importar el dump
mysql -u root -p mantenimiento_industrial < database/mantenimiento_industrial.sql
```

### Opción 2: Usar migraciones de Django (para desarrollo)

```bash
# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
```

## Generar el Dump (antes de entregar)

```bash
# Exportar estructura + datos
mysqldump -u root -p mantenimiento_industrial > database/mantenimiento_industrial.sql
```

**Nota:** El archivo `mantenimiento_industrial.sql` se generará al final del desarrollo con todos los datos de prueba.
