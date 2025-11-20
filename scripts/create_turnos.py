#!/usr/bin/env python3
"""Crear turnos para tener al menos N turnos (por defecto 16).

Uso:
  python ./scripts/create_turnos.py [N]

Ejemplo:
  python ./scripts/create_turnos.py 16

El script crea turnos con fechas futuras si faltan para llegar a N.
No modifica ni renumera IDs existentes.
"""
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add project root to sys.path so `from app import ...` works when running this script
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.turno_service import TurnoService
from app.models import Turno


def main():
    target = 16
    if len(sys.argv) >= 2:
        try:
            target = int(sys.argv[1])
        except ValueError:
            print('Parámetro inválido, usando 16 por defecto.')

    app = create_app('development')
    created = []
    with app.app_context():
        turnos = TurnoService.read_all()
        existing = len(turnos)
        print(f'Turnos actuales: {existing}. Objetivo: {target}.')
        if existing >= target:
            print('No hay turnos para crear.')
            return

        # Determine last date to schedule after
        fechas = [t.fecha for t in turnos if getattr(t, 'fecha', None)]
        if fechas:
            last = max(fechas)
        else:
            last = datetime.now()

        # Create missing turnos spaced 1 hour apart after `last`
        missing = target - existing
        for i in range(1, missing + 1):
            nueva = Turno()
            nueva.fecha = last + timedelta(hours=i)
            nueva.estado = 'disponible'
            creada = TurnoService.create(nueva)
            created.append(creada.id)

    if created:
        print(f'Creado(s) {len(created)} turno(s). IDs: {created}')
    else:
        print('No se crearon turnos.')


if __name__ == '__main__':
    main()
