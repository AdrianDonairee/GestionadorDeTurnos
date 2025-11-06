from app.models import Turno
from app.repositories.turno_repository import TurnoRepository
from typing import List

class TurnoService:
    # Servicio para operaciones sobre Turno

    @staticmethod
    # Asignar estado/cliente al turno
    def asignar_cliente(turno: Turno, estado: str) -> None:
        turno.estado = estado

    @staticmethod
    # Crear un nuevo turno
    def create(turno: Turno) -> Turno:
        repo = TurnoRepository()
        repo.save(turno)
        return turno

    @staticmethod
    # Obtener turno por id
    def get_by_id(id: int) -> Turno:
        repo = TurnoRepository()
        return repo.get_by_id(id)

    @staticmethod
    # Leer todos los turnos
    def read_all() -> List[Turno]:
        repo = TurnoRepository()
        return repo.get_all()

    @staticmethod
    # Actualizar un turno existente
    def update(turno: Turno) -> Turno:
        repo = TurnoRepository()
        return repo.update(turno)

    @staticmethod
    # Eliminar un turno por id
    def delete(id: int) -> None:
        repo = TurnoRepository()
        repo.delete_by_id(id)

