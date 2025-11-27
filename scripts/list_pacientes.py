"""Listar pacientes con sus ids.

Uso:
    # asegúrate de usar el mismo Python/venv (ver prompt .venv)
    python -m pip install --upgrade pip
    python -m pip install Flask Flask-SQLAlchemy flask-marshmallow marshmallow marshmallow-sqlalchemy python-dotenv psycopg[binary] sqlalchemy    python ./scripts/list_pacientes.py

Imprime id, nombre, apellido, dni y email de cada paciente en la BD.
"""
import sys
from pathlib import Path

ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.paciente_service import PacienteService


def main():
    app = create_app('development')
    with app.app_context():
        pacientes = PacienteService.read_all()
        if not pacientes:
            print('No hay pacientes.')
            return
        print('Pacientes:')
        for p in pacientes:
            nombre = f"{getattr(p, 'nombre', '')} {getattr(p, 'apellido', '')}".strip()
            print(f"id={getattr(p, 'id', None)} | {nombre} | DNI={getattr(p, 'dni', None)} | email={getattr(p, 'email', None)}")


if __name__ == '__main__':
    main()
