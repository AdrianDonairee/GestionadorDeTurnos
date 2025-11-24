#!/usr/bin/env python3
"""CLI interactivo para gestionar turnos desde la terminal.

Functions:
- Mostrar turnos disponibles
- Reservar un turno (crear paciente o usar existente)
- Cancelar un turno
- Listar reservas
"""
from datetime import datetime
import sys
import os
import shutil
from pathlib import Path
import re

"""Añadimos la raíz del proyecto a `sys.path` para que los imports del
paquete `app` funcionen cuando se ejecuta el script directamente desde
la carpeta `scripts/` (útil en desarrollo y pruebas)."""
ROOT = str(Path(__file__).resolve().parents[1])
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from app import create_app
from app.services.turno_service import TurnoService
from app.services.paciente_service import PacienteService
from app.models import Paciente, Turno

"""Colores ANSI simples: mejoran la legibilidad en la terminal y ayudan a
destacar errores/confirmaciones; orientado a terminales modernos que
soporten secuencias ANSI."""
RESET = '\x1b[0m'
BOLD = '\x1b[1m'
FG_CYAN = '\x1b[36m'
FG_GREEN = '\x1b[32m'
FG_YELLOW = '\x1b[33m'
FG_RED = '\x1b[31m'
FG_MAGENTA = '\x1b[35m'
FG_BLUE = '\x1b[34m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def section_header(title: str, width: int = 60):
    """Imprime un encabezado de sección con borde pequeño y colores."""
    w = max(40, min(width, shutil.get_terminal_size((80, 20)).columns - 10))
    line = '─' * (w - 4)
    print('\n' + FG_CYAN + BOLD + f'┌{line}┐' + RESET)
    print(FG_CYAN + BOLD + f'│{title.center(w - 4)}│' + RESET)
    print(FG_CYAN + BOLD + f'└{line}┘' + RESET)
    print()


def pause_after_action():
    """Pausa tras una acción. Devuelve True si el usuario quiere salir ('5')."""
    s = input(FG_YELLOW + "Presiona ENTER para volver al menú (o escribe '5' para salir): " + RESET).strip()
    return s == '5'
def print_menu():
    """Presentación del menú principal con borde y colores.

    El uso de un docstring aquí hace explícito el propósito visual del
    método para futuros mantenedores.
    """
    cols = shutil.get_terminal_size((80, 20)).columns
    cols = max(50, min(cols, 100))
    title = 'Gestor de Turnos - Médicos'
    line = '═' * (cols - 4)
    print('\n' + FG_CYAN + BOLD + f'╔{line}╗' + RESET)
    print(FG_CYAN + BOLD + f'║{title.center(cols - 4)}║' + RESET)
    print(FG_CYAN + BOLD + f'╚{line}╝' + RESET)
    print()
    print(FG_YELLOW + 'Elige una opción (escribe el número y pulsa ENTER):' + RESET)
    print()
    print(FG_GREEN + ' 1) ' + RESET + 'Mostrar turnos disponibles')
    print(FG_GREEN + ' 2) ' + RESET + 'Reservar un turno')
    print(FG_GREEN + ' 3) ' + RESET + 'Cancelar un turno')
    print(FG_GREEN + ' 4) ' + RESET + 'Listar reservas')
    print(FG_RED +   ' 5) ' + RESET + 'Salir')
    print()
    print()


def mostrar_turnos_disponibles():
    """Muestra los turnos con estado 'disponible'.

    Ordenamos por `id` para presentar los turnos de forma determinista
    (1..N) y evitar resultados intermitentes en la UI o en tests.
    """
    turnos = TurnoService.read_all()
    disponibles = [t for t in turnos if getattr(t, 'estado', 'disponible') == 'disponible']
    disponibles.sort(key=lambda t: getattr(t, 'id', 0))
    clear_screen()
    if not disponibles:
        print(FG_YELLOW + 'No hay turnos disponibles.' + RESET)
        return pause_after_action()
    section_header('Turnos disponibles')
    print(FG_MAGENTA + BOLD + f"{'ID'.ljust(6)} {'Fecha'.ljust(20)} {'Agenda'.ljust(10)} {'Estado'.ljust(12)}" + RESET)
    print('-' * 60)
    for t in disponibles:
        fecha = t.fecha.strftime('%Y-%m-%d %H:%M') if getattr(t, 'fecha', None) else 'sin fecha'
        estado = getattr(t, 'estado', 'desconocido')
        color = FG_GREEN if estado == 'disponible' else FG_RED
        print(color + f"{str(t.id).ljust(6)} {fecha.ljust(20)} {str(getattr(t,'agenda_id',None)).ljust(10)} {estado.ljust(12)}" + RESET)
    print()
    return pause_after_action()


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

    """Solicitar explícitamente 's' o 'n' y rechazar respuestas inválidas."""
    while True:
        ans = input('Usar paciente existente? (s/N): ').strip().lower()
        if ans in ('s', 'n'):
            usar_existente = (ans == 's')
            break
        print(FG_RED + "Respuesta inválida. Responda 's' o 'n'." + RESET)
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
        """Crear un paciente nuevo.

        Normalizamos y validamos los campos antes de persistir para evitar
        errores en la capa de persistencia (p. ej. DNI/telefono con
        caracteres no numéricos o longitudes fuera de rango).
        """
        p = Paciente()
        p.nombre = input('Nombre: ').strip()
        p.apellido = input('Apellido: ').strip()
        """Pedir y normalizar el DNI: se extraen sólo dígitos para permitir
        que el usuario escriba separadores visuales (puntos, espacios), pero
        se persiste una forma consistente (solo dígitos, max 10)."""
        while True:
            dni_raw = input('DNI (hasta 8 dígitos): ').strip()
            dni_digits = ''.join(ch for ch in dni_raw if ch.isdigit())
            if len(dni_digits) == 0:
                print(FG_RED + 'DNI inválido. Debe contener al menos 1 dígito.' + RESET)
                continue
            if len(dni_digits) > 8:
                print(FG_RED + 'DNI demasiado largo. Máximo 8 dígitos.' + RESET)
                continue
            p.dni = dni_digits
            break
        """Validar el email usando una expresión regular simple; repetir
        hasta obtener una entrada válida para evitar errores posteriores.
        """
        while True:
            email_raw = input('Email: ').strip()
            """Validación básica: patrón user@dominio.tld sin espacios."""
            if re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email_raw):
                p.email = email_raw
                break
            print(FG_RED + 'Email inválido. Introduzca un email con formato válido (ej: usuario@dominio.com).' + RESET)
        """Solicitar la fecha de nacimiento en formato `YYYY-MM-DD` y repetir
        hasta recibir una entrada válida. Esto evita excepciones al parsear
        fechas en capas superiores y garantiza consistencia del dato."""
        while True:
            fd = input('Fecha de nacimiento (YYYY-MM-DD): ').strip()
            try:
                p.fechadenacimiento = datetime.strptime(fd, '%Y-%m-%d').date()
                break
            except Exception:
                print(FG_RED + 'Fecha inválida. Introduzca de nuevo en formato YYYY-MM-DD.' + RESET)
        """Solicitar y normalizar el teléfono a sólo dígitos. Requerimos
        exactamente 10 dígitos para mantener el formato del sistema y
        facilitar futuras integraciones (SMS, etc.)."""
        while True:
            tel_raw = input('Teléfono (10 dígitos): ').strip()
            """Extraer sólo dígitos del teléfono para permitir separadores
            visuales (espacios, guiones) pero persistir una forma
            consistente: solo dígitos."""
            digits = ''.join(ch for ch in tel_raw if ch.isdigit())
            if len(digits) != 10:
                print(FG_RED + 'Teléfono inválido. Debe contener exactamente 10 dígitos.' + RESET)
                continue
            p.telefono = digits
            break
        paciente = PacienteService.create(p)
        print(f'Paciente creado id={paciente.id}')

    """Asignar el paciente creado/seleccionado al turno y marcarlo
    como reservado en la capa de negocio."""
    turno.paciente = paciente
    turno.paciente_id = paciente.id
    TurnoService.asignar_cliente(turno, 'reservado')
    TurnoService.update(turno)
    print(FG_GREEN + f'✅ Turno {turno.id} reservado para {paciente.nombre} {paciente.apellido}.' + RESET)
    return pause_after_action()


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
    print(FG_GREEN + f'✅ Turno {tid} cancelado y vuelto a disponible.' + RESET)
    return pause_after_action()


def listar_reservas():
    """Lista las reservas (turnos no disponibles) ordenadas por id.

    Ordenar por `id` proporciona una vista estable y fácil de seguir para
    el operador cuando revisa reservas consecutivas.
    """
    clear_screen()
    turnos = TurnoService.read_all()
    reservados = [t for t in turnos if getattr(t, 'estado', None) and t.estado != 'disponible']
    """Ordenar por id para presentar las reservas en orden estable y
    fácil de seguir para el operador."""
    reservados.sort(key=lambda t: getattr(t, 'id', 0))
    section_header('Reservas')
    if not reservados:
        print(FG_YELLOW + 'No hay reservas.' + RESET)
        return pause_after_action()
    print(FG_MAGENTA + BOLD + f"{'ID'.ljust(6)} {'Fecha'.ljust(20)} {'Paciente'.ljust(25)} {'Estado'.ljust(12)}" + RESET)
    print('-' * 80)
    for t in reservados:
        fecha = t.fecha.strftime('%Y-%m-%d %H:%M') if getattr(t, 'fecha', None) else 'sin fecha'
        paciente = getattr(t, 'paciente', None)
        if paciente:
            nombre = f"{paciente.nombre} {paciente.apellido} (id={paciente.id})"
        else:
            nombre = f"Paciente id={t.paciente_id}"
        estado = getattr(t, 'estado', 'desconocido')
        print(FG_GREEN + f"{str(t.id).ljust(6)} {fecha.ljust(20)} {nombre.ljust(25)} {estado.ljust(12)}" + RESET)
    print()
    return pause_after_action()


def main():
    app = create_app('development')
    with app.app_context():
        try:
            while True:
                print_menu()
                try:
                    opt = input('> ').strip()
                except (KeyboardInterrupt, EOFError):
                    print('\n' + FG_YELLOW + 'Interrumpido por el usuario. Saliendo...' + RESET)
                    break

                if opt == '1':
                    post = mostrar_turnos_disponibles()
                elif opt == '2':
                    post = reservar_turno()
                elif opt == '3':
                    post = cancelar_turno()
                elif opt == '4':
                    post = listar_reservas()
                elif opt == '5':
                    print('Adiós.')
                    break
                else:
                    print('Opción inválida.')
                    post = None

                if post:
                    print('Adiós.')
                    break
        except Exception:
            print(FG_RED + 'Se produjo un error inesperado. Saliendo.' + RESET)
            


if __name__ == '__main__':
    main()
