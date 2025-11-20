# Sistema de Gestión de Turnos - Consultorio Médico

Proyecto desarrollado para la materia Diseño de Sistemas. El sistema permite administrar turnos médicos de forma sencilla, simulando las operaciones básicas de un consultorio.

## Descripción

El sistema está orientado a la gestión de turnos médicos, permitiendo a los actores interactuar de la siguiente manera:

- **Recepcionista:** Gestiona turnos, consulta disponibilidad, reprograma y accede al historial.
- **Paciente:** Solicita, cancela y consulta turnos disponibles.

## Casos de Uso

- Solicitar turno
- Cancelar turno
- Consultar disponibilidad
- Reprogramación automática de turnos
- Historial de turnos

## Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Framework:** Flask
- **Base de datos:** Postgesql
- **Interfaz:** Consola o interfaz mínima con Tkinter
- **Contenedores:** Docker
- **IDE:** Visual Studio
- **Control de versiones:** GitHub
- **Metodología:** Scrum

## Instalación y Ejecución

1. Clonar el repositorio desde GitHub.
2. Configurar el entorno virtual de Python.
3. Instalar dependencias con `pip install -r requirements.txt`.
4. Levantar la base de datos MySQL (puede usarse Docker).
5. Ejecutar la aplicación con Flask.

## Pasos para configurar tu entorno de trabajo con `uv`

1. Abrir **PowerShell como administrador**.  
2. Instalar `uv`:
   ```powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
Reiniciar la PC.

Abrir el proyecto en Visual Studio Code.

Abrir la terminal en VS Code.

Verificar que uv está instalado:

uv

Crear un entorno virtual con uv:

uv venv

Instalar dependencias necesarias:

uv add flask==3.1.1
uv add python-dotenv==1.1.1

para actualizar dependencias en el proyecto
uv sync para sincronizar

uv add "Flask-SQLAlchemy==3.1.1"
uv add 'mysql-connector-python==9.4.0'

## ejecutar proyecto en modo desarrollo
uv run python .\scripts\run_gestion_turnos.py

## Integrantes

- Bravo Gastón
- Vilchez Franco
- Echevarria Matias
- Diaz Cristopher
- Donaire Adrián

## Uso del CLI `manage.py` (operaciones desde la terminal)

Se agregó un script `manage.py` en la raíz del proyecto para ejecutar tareas comunes desde PowerShell.

Ejemplos de uso (ejecutar desde la carpeta del proyecto con el venv activado):

- Ver ayuda / listar comandos:
```powershell
python manage.py --help
```

- Crear las tablas de la base de datos (según `development` en `app/config/config.py`):
```powershell
python manage.py init-db
```

- Eliminar todas las tablas (útil en pruebas manuales):
```powershell
python manage.py drop-db
```

- Poblado de ejemplo (seed): crea dos pacientes de ejemplo:
```powershell
python manage.py seed
```

- Listar pacientes:
```powershell
python manage.py list-pacientes
```

- Crear un paciente desde la terminal:
```powershell
python manage.py create-paciente --nombre "Luis" --apellido "Lopez" --dni "11122333" --email "luis.lopez@example.com" --fechadenacimiento 1992-04-23 --telefono "+34123456700"
```

- Obtener un paciente por id:
```powershell
python manage.py get-paciente 1
```

- Eliminar paciente por id:
```powershell
python manage.py delete-paciente 1
```

- Levantar servidor de desarrollo (usa `development`):
```powershell
python manage.py runserver --host 0.0.0.0 --port 5000 --debug
```

Notas:
- `manage.py` usa por defecto el contexto `development` al ejecutar comandos. Si quieres ejecutar sobre `testing` o `production`, pregunta y añado una opción `--context` para elegirlo.
- Asegúrate de activar el entorno virtual antes de ejecutar los comandos: `.\.venv\Scripts\Activate`.
- Si ves advertencias de marshmallow/flask-marshmallow, instala las dependencias en el venv con:
```powershell
python -m pip install marshmallow==3.19.0 marshmallow-sqlalchemy==0.29.0
```
