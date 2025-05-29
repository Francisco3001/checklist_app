# 📝 Checklist App

Este proyecto es una aplicación web simple de checklist que permite a los usuarios registrarse, iniciar sesión y gestionar ítems (tareas). Cuenta con una API REST construida con Flask y una base de datos PostgreSQL.

Incluye:
- Autenticación JWT
- Endpoints protegidos
- Testing automático con `pytest`
- Entorno de producción y entorno de testing separados mediante Docker

---
## Requisitos para la ejecución
- Docker
- Python 3.13


## Ejecución del proyecto

### ▶️ Levantar la aplicación y las bases de datos

Para ejecutar la app junto con las bases de datos (producción y testing), asegurate de tener Docker y Docker Compose instalados.

```bash
docker compose up --build -d
```
### Esto levanta:

- La API Flask
- La base de datos de producción (checklistdb)
- La base de datos de testing (checklist_test)

### Ejecutar los tests

⚠️ La base de datos de testing (checklist_test) debe estar corriendo antes de ejecutar los tests.

#### 1. Crear un entorno virtual
```bash
python -m venv .venv
```

#### 2. Activar el entorno virtual
En Windows (PowerShell):
```bash
.\.venv\Scripts\activate
```
En Linux/macOS:

```bash
source .venv/bin/activate
```

#### 3. Instalar dependencias
```bash
pip install -r app/requirements.txt
```

#### 4. Ejecutar tests con pytest
```bash
pytest
```


# 🧪 Notas
- El archivo .env contiene tanto las variables de entorno para producción como para testing.
- La base de datos de testing escucha en el puerto 5433, y la de producción en el 5432.