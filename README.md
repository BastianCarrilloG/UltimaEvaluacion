# API RESTful - Sistema de Mantenimiento Industrial

API desarrollada con Django REST Framework para gestionar empresas clientes, equipos, técnicos, planes de mantención y órdenes de trabajo.

---

## 🛠️ Stack Tecnológico

- **Python 3.10+**
- **Django 5.0.1**
- **Django REST Framework 3.14.0**
- **MySQL 8.0+**
- **Token Authentication**

---

## 📦 Instalación

### 1. Clonar repositorio
```bash
git clone https://github.com/BastianCarrilloG/UltimaEvaluacion.git
cd UltimaEvaluacion
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

### 3. Configurar base de datos

#### Opción A: Importar desde MySQL Workbench (Recomendado)

1. **Abrir MySQL Workbench** y conectarse al servidor

2. **Crear la base de datos:**
   - Click en el ícono de SQL (⚡) o abrir una nueva SQL Tab
   - Ejecutar:
   ```sql
   CREATE DATABASE mantenimiento_industrial CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. **Importar el archivo SQL:**
   - Ir a **Server** → **Data Import**
   - Seleccionar **"Import from Self-Contained File"**
   - Click en **"..."** y buscar: `database/mantenimiento_industrial.sql`
   - En **"Default Target Schema"** seleccionar: `mantenimiento_industrial`
   - Click en **"Start Import"**
   - ✅ Esperar a que termine la importación

4. **Verificar la importación:**
   - Refrescar el panel de SCHEMAS (click derecho → Refresh All)
   - Expandir `mantenimiento_industrial` y verificar las tablas

#### Opción B: Importar desde línea de comandos

```bash
# Crear base de datos
mysql -u root -p
```
```sql
CREATE DATABASE mantenimiento_industrial CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit;
```
```bash
# Importar dump
mysql -u root -p mantenimiento_industrial < database/mantenimiento_industrial.sql
```

#### Opción C: Crear desde cero con migraciones

**Configurar credenciales en `config/settings.py`:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mantenimiento_industrial',
        'USER': 'root',
        'PASSWORD': 'tu_contraseña',  # ⚠️ Cambiar aquí
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

**Ejecutar migraciones:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Crear superusuario (IMPORTANTE)

**Si importaste el dump SQL, ya tienes usuarios creados. Si no, crea uno:**

```bash
python manage.py createsuperuser
```

Te pedirá:
- Username
- Email (opcional)
- Password

### 5. Ejecutar servidor
```bash
python manage.py runserver
```

**API disponible en:** `http://127.0.0.1:8000/api/`

---

## 📁 Estructura del Proyecto

```
UltimaEvaluacion/
├── api/
│   ├── models.py           # 5 modelos (Empresa, Equipo, Técnico, PlanMantencion, OrdenTrabajo)
│   ├── serializers.py      # Serializers para JSON
│   ├── views.py            # ViewSets con CRUD
│   ├── urls.py             # Rutas de la API
│   ├── validators.py       # Validadores (RUT, teléfono, número de serie)
│   ├── permissions.py      # Control de acceso
│   └── admin.py            # Panel de administración
├── config/
│   ├── settings.py         # Configuración DRF y BD
│   └── urls.py             # URLs principales
├── database/
│   └── mantenimiento_industrial.sql
└── requirements.txt
```

---

## 🌐 Endpoints de la API

### Recursos principales

| Recurso | Endpoint | Métodos |
|---------|----------|---------|
| Empresas | `/api/empresas/` | GET, POST, PUT, PATCH, DELETE |
| Equipos | `/api/equipos/` | GET, POST, PUT, PATCH, DELETE |
| Técnicos | `/api/tecnicos/` | GET, POST, PUT, PATCH, DELETE |
| Planes de Mantención | `/api/planes-mantencion/` | GET, POST, PUT, PATCH, DELETE |
| Órdenes de Trabajo | `/api/ordenes-trabajo/` | GET, POST, PUT, PATCH, DELETE |

### Endpoints especiales

- **Estado de la API:** `GET /api/estado/`
- **Autenticación:** `POST /api/auth/login/`
- **Panel Admin:** `http://127.0.0.1:8000/admin/`
- **API Root:** `http://127.0.0.1:8000/api/`

### Filtros disponibles

```
GET /api/equipos/?empresa=1
GET /api/planes-mantencion/?equipo=1&activo=true
GET /api/ordenes-trabajo/?estado=pendiente&tecnico=1
```

---

## 🔐 Autenticación

### Obtener token (vía API)

```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}
```

**Respuesta:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Usar el token

```http
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Permisos

- **No autenticado:** Solo lectura (GET)
- **Autenticado:** CRUD completo (GET, POST, PUT, PATCH, DELETE)

---

## 🧪 Cómo Probar la API

### Opción 1: API Navegable (Más fácil)

1. Ve a: `http://127.0.0.1:8000/api/empresas/`
2. Click en **"Log in"** (arriba a la derecha)
3. Ingresa con tu superusuario
4. Verás un formulario al final de la página para hacer POST
5. Llena los campos y click en **"POST"**

### Opción 2: Panel de Administración

1. Ve a: `http://127.0.0.1:8000/admin/`
2. Ingresa con tu superusuario
3. Gestiona todas las entidades desde la interfaz visual

### Opción 3: cURL (Línea de comandos)

**Primero obtén tu token:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "tu_password"}'
```

**Luego usa el token para crear:**
```bash
curl -X POST http://127.0.0.1:8000/api/empresas/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token tu_token_aqui" \
  -d '{
    "nombre": "Industrias S.A.",
    "direccion": "Av. Principal 123",
    "rut": "76.123.456-7"
  }'
```

### Opción 4: Postman o Insomnia

1. Descarga [Postman](https://www.postman.com/) o [Insomnia](https://insomnia.rest/)
2. Crea una petición POST a `http://127.0.0.1:8000/api/empresas/`
3. En Headers agrega: `Authorization: Token tu_token`
4. En Body (JSON) agrega los datos

---

## 📊 Modelos de Datos

### Empresa
- `nombre` (CharField)
- `direccion` (CharField)
- `rut` (CharField, unique, validado)
- `fecha_creacion` (DateTimeField, auto)

### Equipo
- `empresa` (ForeignKey → Empresa)
- `nombre` (CharField)
- `numero_serie` (CharField, unique, validado)
- `critico` (BooleanField)
- `fecha_instalacion` (DateField)

### Técnico
- `usuario` (OneToOneField → User)
- `nombre_completo` (CharField)
- `especialidad` (CharField)
- `telefono` (CharField, validado)

### PlanMantencion
- `equipo` (ForeignKey → Equipo)
- `nombre` (CharField)
- `frecuencia_dias` (PositiveIntegerField)
- `activo` (BooleanField)

### OrdenTrabajo
- `plan` (ForeignKey → PlanMantencion)
- `equipo` (ForeignKey → Equipo)
- `tecnico` (ForeignKey → Técnico, nullable)
- `estado` (CharField: pendiente, en_progreso, completada, cancelada)
- `fecha_programada` (DateField)
- `fecha_completada` (DateTimeField, nullable)
- `notas` (TextField)

---

## ⚙️ Configuración DRF

```python
# config/settings.py
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d/%m/%Y %H:%M:%S',
    'DATE_FORMAT': '%d/%m/%Y',
}
```

---

## 🧪 Validaciones Personalizadas

- **RUT Chileno:** Formato `12.345.678-9` con validación de dígito verificador
- **Teléfono Chileno:** Formato `+56912345678` o `912345678`
- **Número de Serie:** 5-50 caracteres alfanuméricos

---

## 📝 Ejemplos de Uso

### Crear empresa
```bash
curl -X POST http://127.0.0.1:8000/api/empresas/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token tu_token" \
  -d '{
    "nombre": "Industrias S.A.",
    "direccion": "Av. Principal 123",
    "rut": "76.123.456-7"
  }'
```

### Listar equipos de una empresa
```bash
curl http://127.0.0.1:8000/api/equipos/?empresa=1
```

### Crear orden de trabajo
```bash
curl -X POST http://127.0.0.1:8000/api/ordenes-trabajo/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token tu_token" \
  -d '{
    "plan": 1,
    "equipo": 1,
    "tecnico": 1,
    "estado": "pendiente",
    "fecha_programada": "20/12/2024",
    "notas": "Mantención preventiva"
  }'
```

---


