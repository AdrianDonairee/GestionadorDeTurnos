#!/usr/bin/env python3
"""Listar todos los turnos con información básica.

Uso:
    python ./scripts/list_turnos.py

Este script añade automáticamente la raíz del proyecto a `sys.path`
para permitir imports relativos a `app` cuando se ejecuta desde
la carpeta `scripts/` (útil en desarrollo).
"""
import sys
from pathlib import Path

ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.turno_service import TurnoService


def main():
    app = create_app('development')
    with app.app_context():
        turnos = TurnoService.read_all()
        """ Asegurar orden determinista por `id` para mostrar 1..N"""
        try:
            turnos = sorted(turnos, key=lambda t: getattr(t, 'id', 0))
        except Exception:
            """Si los objetos no son iterables/directamente ordenables, dejar como vinieron"""
            pass
        print(f'Total turnos: {len(turnos)}')
        for t in turnos:
            fecha = t.fecha.strftime('%Y-%m-%d %H:%M') if getattr(t, 'fecha', None) else 'sin fecha'
            print(f"ID={t.id} | Fecha={fecha} | Agenda={getattr(t,'agenda_id',None)} | Paciente={getattr(t,'paciente_id',None)} | Estado={getattr(t,'estado',None)}")


if __name__ == '__main__':
    main()
