#!/usr/bin/env python
"""
CLI minimal para administrar la aplicación desde la terminal.

Comandos disponibles:
- runserver     : Inicia la app Flask en modo desarrollo
- init-db       : Crea las tablas de la base de datos
- drop-db       : Elimina las tablas de la base de datos
- create-paciente: Crea un paciente (requiere nombre, apellido, dni, email, fechadenacimiento YYYY-MM-DD, telefono)
- list-pacientes : Muestra todos los pacientes
- get-paciente   : Muestra un paciente por id
- delete-paciente: Elimina un paciente por id
- seed           : Pobla la BD con datos de ejemplo (opcional)

Uso: python manage.py <comando> [opciones]
"""
import argparse
from datetime import datetime
from app import create_app, db
from sqlalchemy.exc import OperationalError

"""Importar modelos y servicios dentro del contexto del proyecto."""
from app.models import Paciente, Turno
from app.services.paciente_service import PacienteService
from app.services.turno_service import TurnoService
from datetime import timedelta


def with_app_context(func):
    """Decorador simple para ejecutar funciones dentro de app.app_context()."""
    def wrapper(*args, **kwargs):
        app = create_app('development')
        with app.app_context():
            return func(*args, **kwargs)
    return wrapper


@with_app_context
def init_db(args):
    try:
        db.create_all()
        print("Base de datos inicializada (tablas creadas).")
    except OperationalError as e:
        print("Error conectando a la base de datos:", str(e))
        print()
        print("Sugerencias:")
        print(" - Compruebe que Postgres esté arrancado y accesible en la URI configurada.")
        print(" - Si está usando Docker, ejecute: docker-compose up -d y verifique los logs del contenedor de Postgres.")
        print(" - Para evitar depender de Postgres en desarrollo temporalmente, use SQLite: setee DEV_DATABASE_URI='sqlite:///dev.db' y vuelva a ejecutar init-db.")
        print()
        return


@with_app_context
def drop_db(args):
    db.drop_all()
    print("Tablas eliminadas de la base de datos.")


@with_app_context
def runserver(args):
    app = create_app('development')
    app.run(host=args.host, port=args.port, debug=args.debug)


@with_app_context
def create_paciente(args):
    """Crear una instancia de `Paciente` a partir de los argumentos
    de la línea de comandos y persistirla mediante el servicio.
    Valida el formato de la fecha antes de crear la entidad."""
    try:
        fecha = datetime.strptime(args.fechadenacimiento, "%Y-%m-%d").date()
    except Exception as e:
        print("Formato de fecha inválido. Use YYYY-MM-DD.")
        return

    paciente = Paciente()
    paciente.nombre = args.nombre
    paciente.apellido = args.apellido
    paciente.dni = args.dni
    paciente.email = args.email
    paciente.fechadenacimiento = fecha
    paciente.telefono = args.telefono

    saved = PacienteService.create(paciente)
    print(f"Paciente creado. id={getattr(saved, 'id', None)} Nombre={saved.nombre} {saved.apellido}")


@with_app_context
def list_pacientes(args):
    pacientes = PacienteService.read_all()
    if not pacientes:
        print("No hay pacientes.")
        return
    for p in pacientes:
        print(f"{p.id}: {p.nombre} {p.apellido} - DNI: {p.dni} - Tel: {p.telefono}")


@with_app_context
def get_paciente(args):
    p = PacienteService.get_by_id(args.id)
    if not p:
        print(f"Paciente {args.id} no encontrado.")
        return
    print(f"{p.id}: {p.nombre} {p.apellido} - DNI: {p.dni} - Email: {p.email} - FechaNacimiento: {p.fechadenacimiento} - Tel: {p.telefono}")


@with_app_context
def delete_paciente(args):
    ok = PacienteService.delete(args.id)
    if ok:
        print(f"Paciente {args.id} eliminado.")
    else:
        print(f"Paciente {args.id} no encontrado o no pudo eliminarse.")


@with_app_context
def seed(args):
    """Poblar la base de datos con un conjunto mínimo de pacientes
    de ejemplo (útil para pruebas locales)."""
    p1 = Paciente()
    p1.nombre = "Juan"
    p1.apellido = "Perez"
    p1.dni = "10987654"
    p1.email = "juan.perez@example.com"
    p1.fechadenacimiento = datetime(1990,1,1).date()
    p1.telefono = "2604456789"
    PacienteService.create(p1)

    p2 = Paciente()
    p2.nombre = "Ana"
    p2.apellido = "Gomez"
    p2.dni = "87654321"
    p2.email = "ana.gomez@example.com"
    p2.fechadenacimiento = datetime(1985,6,15).date()
    p2.telefono = "2604222333"
    PacienteService.create(p2)

    p3 = Paciente()
    p3.nombre = "Lucas"
    p3.apellido = "Gimenez"
    p3.dni = "44123456"
    p3.email = "lucas.gimenez@example.com"
    p3.fechadenacimiento = datetime(1990,1,1).date()
    p3.telefono = "+2604456789"
    PacienteService.create(p3)
    print("Seed completado: 3 pacientes creados.")


@with_app_context
def seed_turnos(args):
    """Crear turnos de ejemplo en fechas próximas para pruebas o demo.
    Los horarios se generan a partir de la fecha/hora actual.
    """
    from datetime import datetime
    now = datetime.now()
    created = 0
    for i in range(1, 9):
        t = Turno()
        """Generar horarios rotativos en franjas de mañana (9..12) y días
        sucesivos para poblar turnos de ejemplo."""
        t.fecha = (now + timedelta(days=(i-1)//4, hours=9 + ((i-1) % 4))).replace(minute=0, second=0, microsecond=0)
        t.estado = 'disponible'
        """Dejar `agenda_id` en None cuando no existen agendas; si en el
        sistema hay agendas definidas podrían asignarse explícitamente."""
        TurnoService.create(t)
        created += 1
    print(f"Seed-turnos completado: {created} turnos creados.")


def main():
    parser = argparse.ArgumentParser(description="Manage: administracion de GestionadorDeTurnos")
    sub = parser.add_subparsers(dest='command', required=True)

    # runserver
    p_run = sub.add_parser('runserver')
    p_run.add_argument('--host', default='127.0.0.1')
    p_run.add_argument('--port', type=int, default=5000)
    p_run.add_argument('--debug', action='store_true')
    p_run.set_defaults(func=runserver)

    # init-db
    p_init = sub.add_parser('init-db')
    p_init.set_defaults(func=init_db)

    # drop-db
    p_drop = sub.add_parser('drop-db')
    p_drop.set_defaults(func=drop_db)

    # create-paciente
    p_cp = sub.add_parser('create-paciente')
    p_cp.add_argument('--nombre', required=True)
    p_cp.add_argument('--apellido', required=True)
    p_cp.add_argument('--dni', required=True)
    p_cp.add_argument('--email', required=True)
    p_cp.add_argument('--fechadenacimiento', required=True, help='YYYY-MM-DD')
    p_cp.add_argument('--telefono', required=True)
    p_cp.set_defaults(func=create_paciente)

    # list-pacientes
    p_ls = sub.add_parser('list-pacientes')
    p_ls.set_defaults(func=list_pacientes)

    # get-paciente
    p_get = sub.add_parser('get-paciente')
    p_get.add_argument('id', type=int)
    p_get.set_defaults(func=get_paciente)

    # delete-paciente
    p_del = sub.add_parser('delete-paciente')
    p_del.add_argument('id', type=int)
    p_del.set_defaults(func=delete_paciente)

    # seed
    p_seed = sub.add_parser('seed')
    p_seed.set_defaults(func=seed)

    # seed-turnos
    p_st = sub.add_parser('seed-turnos')
    p_st.set_defaults(func=seed_turnos)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
