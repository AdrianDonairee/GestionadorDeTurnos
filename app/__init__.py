import logging
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config import config

db = SQLAlchemy()

def create_app(config_name: str = None) -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    # Si no se pasa config_name, usar FLASK_CONTEXT o 'development' por defecto
    if config_name is None:
        config_name = os.getenv('FLASK_CONTEXT', 'development')

    app = Flask(__name__)
    
    # Cargar la configuración usando la factory
    f = config.factory(config_name)
    app.config.from_object(f)

    # Inicializar la base de datos
    db.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
