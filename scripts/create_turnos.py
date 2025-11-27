"""Crear turnos para tener al menos N turnos (por defecto 16).

Uso:
python ./scripts/create_turnos.py [N]

El script crea turnos con fechas futuras si faltan para llegar a N.
No modifica ni renumera IDs existentes.
"""
import sys
from pathlib import Path
from datetime import datetime, timedelta

"""Añadimos la raíz del proyecto a `sys.path` para permitir imports
relativos a `app` cuando se ejecuta este script desde `scripts/`.
"""
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

        """Determinar la última fecha existente para programar nuevos turnos
        a partir de ella. Si no hay fechas, usar la fecha/hora actual."""
        fechas = [t.fecha for t in turnos if getattr(t, 'fecha', None)]
        if fechas:
            last = max(fechas)
        else:
            last = datetime.now()
        """Crear los turnos faltantes espaciándolos cada 1 hora a partir de
        la última fecha conocida (`last`)."""
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
