#!/usr/bin/env python3
"""Recortar la tabla de `turnos` para que queden solo los N primeros (por fecha).

Por defecto N=16. El script elimina los turnos más antiguos/excedentes.

Uso:
python ./scripts/trim_turnos.py [N]"""

import sys
from pathlib import Path
from typing import List

# Add project root to sys.path so `from app import ...` works when running this script
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.repositories.turno_repository import TurnoRepository
from app.models import Turno


def trim(limit: int = 16) -> List[int]:
    """Mantiene los `limit` primeros turnos ordenados por fecha y elimina el resto.

    Retorna la lista de ids eliminados.
    """
    repo = TurnoRepository()
    all_turnos = repo.get_all()  # ya ordena por fecha
    if len(all_turnos) <= limit:
        return []
    to_delete = all_turnos[limit:]
    deleted_ids = []
    for t in to_delete:
        deleted_ids.append(t.id)
        repo.delete_by_id(t.id)
    return deleted_ids


def main():
    limit = 16
    if len(sys.argv) >= 2:
        try:
            limit = int(sys.argv[1])
        except ValueError:
            print('Parámetro inválido, usando 16 por defecto.')

    app = create_app('development')
    with app.app_context():
        deleted = trim(limit)
        if not deleted:
            print(f'No era necesario recortar. Hay <= {limit} turnos.')
        else:
            print(f'Eliminados {len(deleted)} turnos. IDs: {deleted}')


if __name__ == '__main__':
    main()
