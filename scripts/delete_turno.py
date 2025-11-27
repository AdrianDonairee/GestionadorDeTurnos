"""Eliminar un turno por id desde la CLI.

Uso:
python ./scripts/delete_turno.py <id>"""

import sys
from pathlib import Path

ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.turno_service import TurnoService


def main():
    if len(sys.argv) < 2:
        print('Uso: python ./scripts/delete_turno.py <id>')
        return
    try:
        turno_id = int(sys.argv[1])
    except ValueError:
        print('El id debe ser un número entero.')
        return

    app = create_app('development')
    with app.app_context():
        TurnoService.delete(turno_id)
        print(f'Turno {turno_id} (si existía) ha sido eliminado.')


if __name__ == '__main__':
    main()
