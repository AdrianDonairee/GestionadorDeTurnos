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
- **Base de datos:** MySQL (servidor)
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
uv run flask run

## Integrantes

- Bravo Gastón
- Vilchez Franco
- Echevarria Matias
- Diaz Cristopher
- Donaire Adrián