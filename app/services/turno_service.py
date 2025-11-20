from app.models import Turno
from app.repositories.turno_repository import TurnoRepository
from typing import List

"""Servicio de alto nivel para operaciones con `Turno`.

Provee métodos estáticos para crear, leer, actualizar y eliminar turnos,
delegando en `TurnoRepository`.
"""


class TurnoService:
    @staticmethod
    def asignar_cliente(turno: Turno, estado: str) -> None:
        turno.estado = estado

    @staticmethod
    def create(turno: Turno) -> Turno:
        repo = TurnoRepository()
        repo.save(turno)
        return turno

    @staticmethod
    def get_by_id(id: int) -> Turno:
        """Devuelve el turno identificado por `id` o None."""
        repo = TurnoRepository()
        return repo.get_by_id(id)

    @staticmethod
    def read_all() -> List[Turno]:
        repo = TurnoRepository()
        return repo.get_all()

    @staticmethod
    def update(turno: Turno) -> Turno:
        repo = TurnoRepository()
        return repo.update(turno)

    @staticmethod
    def delete(id: int) -> None:
        repo = TurnoRepository()
        repo.delete_by_id(id)

