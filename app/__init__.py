import logging
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name: str = None) -> Flask:
    """Crear y configurar la instancia de Flask.

    - `config_name`: nombre del entorno (p.ej. 'development' o 'testing').
    Si no se proporciona se toma de la variable `FLASK_CONTEXT` o
    'development' por defecto.
    """
    if config_name is None:
        config_name = os.getenv('FLASK_CONTEXT', 'development')

    app = Flask(__name__)

    """Cargar la configuración a partir de la fábrica de settings.

    Separar la creación de config en una factory permite definir
    ajustes por entorno (development/testing/production).
    """
    f = config.factory(config_name)
    app.config.from_object(f)
    db.init_app(app)
    ma.init_app(app)
    from app.resources import home_bp, paciente_bp
    app.register_blueprint(home_bp, url_prefix='/api/v1')
    app.register_blueprint(paciente_bp, url_prefix='/api/v1')

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
