#!/usr/bin/env python3
"""Eliminar un paciente por id desde la CLI.

Uso:
python ./scripts/delete_paciente.py <id>

Ejemplo:
python ./scripts/delete_paciente.py 3
"""
import sys
from pathlib import Path

# Add project root to sys.path so `from app import ...` works when running this script
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.paciente_service import PacienteService


def main():
    if len(sys.argv) < 2:
        print('Uso: python ./scripts/delete_paciente.py <id>')
        return
    try:
        paciente_id = int(sys.argv[1])
    except ValueError:
        print('El id debe ser un número entero.')
        return

    app = create_app('development')
    with app.app_context():
        deleted = PacienteService.delete(paciente_id)
        if deleted:
            print(f'Paciente {paciente_id} eliminado correctamente.')
        else:
            print(f'Paciente {paciente_id} no encontrado.')


if __name__ == '__main__':
    main()
