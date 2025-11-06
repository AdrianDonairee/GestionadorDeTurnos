import logging
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config import config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
def create_app(config_name: str = None) -> Flask:
    """
    Usando el patrón Application Factory
    Referencia: Book Flask Web Development Page 78
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
    ma.init_app(app)
    from app.resources import home_bp,paciente_bp
    app.register_blueprint(home_bp, url_prefix='/api/v1')
    app.register_blueprint(paciente_bp, url_prefix='/api/v1')
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
