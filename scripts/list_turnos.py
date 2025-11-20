#!/usr/bin/env python3
"""Listar todos los turnos con información básica.

Uso:
  python ./scripts/list_turnos.py
"""
import sys
from pathlib import Path

# Add project root to sys.path so `from app import ...` works when running this script
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.turno_service import TurnoService


def main():
    app = create_app('development')
    with app.app_context():
        turnos = TurnoService.read_all()
        print(f'Total turnos: {len(turnos)}')
        for t in turnos:
            fecha = t.fecha.strftime('%Y-%m-%d %H:%M') if getattr(t, 'fecha', None) else 'sin fecha'
            print(f"ID={t.id} | Fecha={fecha} | Agenda={getattr(t,'agenda_id',None)} | Paciente={getattr(t,'paciente_id',None)} | Estado={getattr(t,'estado',None)}")


if __name__ == '__main__':
    main()
