"""
Script pequeño para comprobar la conexión a la BD y listar hasta 5 pacientes.
Ejecutar desde PowerShell con el entorno virtual activo:

    python ./scripts/check_db.py

"""
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()
uri = os.getenv('DEV_DATABASE_URI') or os.getenv('DEV_DATABASE_URI'.upper())
if not uri:
    print('No se encontró DEV_DATABASE_URI en las variables de entorno.')
    raise SystemExit(1)

print('Conectando a:', uri)
engine = create_engine(uri, connect_args={'connect_timeout': 5})
try:
    with engine.connect() as conn:
        try:
            count = conn.execute(text('SELECT count(*) FROM public.pacientes')).scalar()
        except Exception as e:
            print('Error ejecutando SELECT count(*) FROM public.pacientes:')
            print(e)
            raise
        print('COUNT:', count)
        rows = conn.execute(text('SELECT id, nombre, apellido, dni FROM public.pacientes ORDER BY id DESC LIMIT 5')).fetchall()
        print('ROWS (up to 5):')
        for r in rows:
            print(r)

        """Ahora listar algunos turnos de ejemplo si la tabla existe."""
        try:
            tcount = conn.execute(text('SELECT count(*) FROM public.turnos')).scalar()
            print('\nTURNOS COUNT:', tcount)
            trows = conn.execute(text("SELECT id, fecha, estado, paciente_id, agenda_id FROM public.turnos ORDER BY id DESC LIMIT 10")).fetchall()
            print('TURNOS (up to 10):')
            for tr in trows:
                print(tr)
        except Exception as e:
            print('\nNo se pudo leer la tabla public.turnos:')
            print(e)
finally:
    engine.dispose()

print('\nHecho.')
