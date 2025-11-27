"""Resetear la tabla `turnos` y crear 16 turnos nuevos con IDs 1..16.

USO:
python ./scripts/reset_turnos_to_1_16.py      # pedirá confirmación
python ./scripts/reset_turnos_to_1_16.py --yes  # ejecuta sin pedir confirmación

ADVERTENCIA: Esto BORRA todos los registros de la tabla `turnos` (y puede afectar tablas relacionadas
si existen claves foráneas). Haz backup antes de ejecutar si necesitas conservar datos.
"""
import sys
from pathlib import Path
from datetime import datetime, timedelta

"""Añadimos la raíz del proyecto a `sys.path` para permitir imports
relativos a `app` cuando se ejecuta este script desde la carpeta `scripts/`.
"""
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app, db
from sqlalchemy import text
from app.models import Turno
from app.services.turno_service import TurnoService


def confirm(prompt: str) -> bool:
    resp = input(prompt + ' [s/N]: ').strip().lower()
    return resp == 's' or resp == 'y'


def reset_and_create(target: int = 16):
    """Ejecuta TRUNCATE para reiniciar la tabla `turnos` y la secuencia de IDs,
    luego crea `target` turnos. Usamos SQL directo para TRUNCATE porque es la
    forma segura de reiniciar la secuencia en Postgres."""
    with db.engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE turnos RESTART IDENTITY CASCADE;"))

    """Crear `target` turnos nuevos y devolver sus IDs."""
    created_ids = []
    base = datetime.now()
    for i in range(1, target + 1):
        t = Turno()
        """Distribuir horarios en franjas (9..12) y rotar días para
        generar turnos de ejemplo."""
        t.fecha = base + timedelta(days=(i-1)//4, hours=((i-1)%4) + 9)
        t.estado = 'disponible'
        created = TurnoService.create(t)
        created_ids.append(created.id)
    return created_ids


def main():
    target = 16
    force = False
    if '--yes' in sys.argv or '-y' in sys.argv:
        force = True
    if len(sys.argv) >= 2:
        """Permitir `--yes` y opcionalmente un argumento entero para `target`."""
        for a in sys.argv[1:]:
            if a.lstrip('-').isdigit():
                target = int(a)

    print('ADVERTENCIA: Esto eliminará TODOS los turnos y recreará', target, 'turnos nuevos con IDs 1..N.')
    if not force:
        ok = confirm('¿Continuar?')
        if not ok:
            print('Operación cancelada por el usuario.')
            return

    app = create_app('development')
    with app.app_context():
        created = reset_and_create(target)
        print(f'Creados {len(created)} turnos. IDs: {created}')


if __name__ == '__main__':
    main()
