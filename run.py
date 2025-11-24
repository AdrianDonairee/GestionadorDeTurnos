"""Punto de entrada usado por servidores WSGI como gunicorn.

Exporta la variable `app` para que gunicorn pueda importarla mediante
la expresión `run:app` o similar.
"""
from app import create_app

app = create_app('production')
