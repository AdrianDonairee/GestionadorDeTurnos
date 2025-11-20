#!/usr/bin/env python3
"""CLI interactivo para gestionar turnos desde la terminal.

Funciones:
- Mostrar turnos disponibles
- Reservar un turno (crear paciente o usar existente)
- Cancelar un turno
- Listar reservas
"""
from datetime import datetime
import sys
import os
from pathlib import Path

# Add project root to sys.path so `from app import ...` works when running this script
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.turno_service import TurnoService
from app.services.paciente_service import PacienteService
from app.models import Paciente, Turno


def print_menu():
    print('\nBienvenido al Gestor de Turnos ')
    print('\nElige una opción:')
    print('1) Mostrar turnos disponibles')
    print('2) Reservar un turno')
    print('3) Cancelar un turno')
    print('4) Listar reservas')
    print('5) Salir')


def mostrar_turnos_disponibles():
    turnos = TurnoService.read_all()
    disponibles = [t for t in turnos if getattr(t, 'estado', 'disponible') == 'disponible']
    if not disponibles:
        print('No hay turnos disponibles.')
        return
    print('\nTurnos disponibles:')
    for t in disponibles:
        fecha = t.fecha.strftime('%Y-%m-%d %H:%M') if hasattr(t, 'fecha') and t.fecha else 'sin fecha'
        print(f"ID={t.id} | Fecha={fecha} | Agenda={getattr(t, 'agenda_id', None)} | Estado={t.estado}")


def reservar_turno():
    try:
        tid = int(input('Id del turno a reservar: ').strip())
    except ValueError:
        print('Id inválido.')
        return
    turno = TurnoService.get_by_id(tid)
    if not turno:
        print('Turno no encontrado.')
        return
    if turno.estado != 'disponible':
        print('El turno no está disponible (estado:', turno.estado, ')')
        return

    usar_existente = input('Usar paciente existente? (s/N): ').strip().lower() == 's'
    paciente = None
    if usar_existente:
        try:
            pid = int(input('Id del paciente: ').strip())
            paciente = PacienteService.get_by_id(pid)
            if not paciente:
                print('Paciente no encontrado.')
                return
        except ValueError:
            print('Id inválido.')
            return
    else:
        # Crear paciente nuevo
        p = Paciente()
        p.nombre = input('Nombre: ').strip()
        p.apellido = input('Apellido: ').strip()
        p.dni = input('DNI: ').strip()
        p.email = input('Email: ').strip()
        fd = input('Fecha de nacimiento (YYYY-MM-DD): ').strip()
        try:
            p.fechadenacimiento = datetime.strptime(fd, '%Y-%m-%d').date()
        except Exception:
            print('Fecha inválida.')
            return
        p.telefono = input('Teléfono: ').strip()
        paciente = PacienteService.create(p)
        print(f'Paciente creado id={paciente.id}')

    # Asignar paciente al turno y cambiar estado
    turno.paciente = paciente
    turno.paciente_id = paciente.id
    TurnoService.asignar_cliente(turno, 'reservado')
    TurnoService.update(turno)
    print(f'Turno {turno.id} reservado para {paciente.nombre} {paciente.apellido}.')


def cancelar_turno():
    try:
        tid = int(input('Id del turno a cancelar: ').strip())
    except ValueError:
        print('Id inválido.')
        return
    turno = TurnoService.get_by_id(tid)
    if not turno:
        print('Turno no encontrado.')
        return
    if turno.estado == 'disponible':
        print('El turno ya está libre.')
        return
    turno.paciente = None
    turno.paciente_id = None
    TurnoService.asignar_cliente(turno, 'disponible')
    TurnoService.update(turno)
    print(f'Turno {tid} cancelado y vuelto a disponible.')


def listar_reservas():
    turnos = TurnoService.read_all()
    reservados = [t for t in turnos if getattr(t, 'estado', None) and t.estado != 'disponible']
    if not reservados:
        print('No hay reservas.')
        return
    print('\nReservas:')
    for t in reservados:
        fecha = t.fecha.strftime('%Y-%m-%d %H:%M') if t.fecha else 'sin fecha'
        paciente = getattr(t, 'paciente', None)
        if paciente:
            nombre = f"{paciente.nombre} {paciente.apellido} (id={paciente.id})"
        else:
            nombre = f"Paciente id={t.paciente_id}"
        print(f"Turno ID={t.id} | Fecha={fecha} | Paciente={nombre} | Estado={t.estado}")


def chat():
    print('\nModo chat. Escribe mensajes (vacío para salir).')
    while True:
        line = input('> ').strip()
        if line == '':
            print('Saliendo de chat.')
            break
        # Para ahora, solo repetimos. Aquí podrías integrar un bot más avanzado.
        print('Bot: ', line)


def main():
    app = create_app('development')
    with app.app_context():
        while True:
            print_menu()
            opt = input('> ').strip()
            if opt == '1':
                mostrar_turnos_disponibles()
            elif opt == '2':
                reservar_turno()
            elif opt == '3':
                cancelar_turno()
            elif opt == '4':
                listar_reservas()
            elif opt == '5':
                print('Adiós.')
                break
            else:
                print('Opción inválida.')


if __name__ == '__main__':
    main()
