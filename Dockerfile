# Dockerfile (simple, apto para desarrollo/pruebas)
FROM python:3.12-slim

# No escribir .pyc y salida sin buffer para logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema necesarias para compilar algunas librerías
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
&& rm -rf /var/lib/apt/lists/*

# Copiar sólo el pyproject para aprovechar cache de Docker
COPY pyproject.toml /app/

# Instalar pip y las dependencias listadas en pyproject (las pongo explícitas
# según tu pyproject.toml; ajusta si cambian versiones)
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir \
    flask==3.1.1 \
    flask-sqlalchemy==3.1.1 \
    flask-marshmallow==1.3.0 \
    marshmallow==3.19.0 \
    marshmallow-sqlalchemy==0.29.0 \
    sqlalchemy==2.0.43 \
    python-dotenv==1.1.1 \
    psycopg[binary]>=3.2.9 \
    pyrefly>=0.29.1 \
    marshmallow-sqlalchemy==0.29.0

# Copiar el resto del proyecto
COPY . /app

# Variables de entorno (ajusta según necesites)
ENV FLASK_CONTEXT=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PROD_DATABASE_URI="sqlite:////app/gestion.db"
EXPOSE 5000

# Comando por defecto (dev/simple). Usa el factory para crear la app.
# Nota: para producción se recomienda usar gunicorn/uvicorn según sea apropiado.
CMD ["python", "-c", "from app import create_app; create_app().run(host='0.0.0.0', port=5000)"]

