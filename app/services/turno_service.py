from app.models import Turno
from app.repositories.turno_repository import TurnoRepository
from typing import List

class TurnoService:
    @staticmethod
    def create(turno: Turno) -> Turno:
        """
        Crea un nuevo turno en la base de datos.
        :param turno: Objeto Turno a crear.
        :return: El objeto Turno creado.
        """
        TurnoRepository.create(turno)
        return turno

    @staticmethod
    def get_by_id(id: int) -> Turno:
        """
        Recupera un turno por su ID.
        :param id: ID del turno a recuperar.
        :return: Objeto Turno si existe, sino None.
        """
        return TurnoRepository.get_by_id(id)

    @staticmethod
    def read_all() -> List[Turno]:
        """
        Recupera todos los turnos de la base de datos.
        :return: Lista de objetos Turno.
        """
        return TurnoRepository.read_all()

    @staticmethod
    def update(turno: Turno) -> Turno:
        """
        Actualiza un turno existente.
        :param turno: Objeto Turno con datos actualizados.
        :return: El turno actualizado.
        """
        TurnoRepository.update(turno)
        return turno

    @staticmethod
    def delete(id: int) -> None:
        """
        Elimina un turno por su ID.
        :param id: ID del turno a eliminar.
        """
        TurnoRepository.delete(id)
