from app.repositories import AgendaRepository
from app.models import Agenda
from datetime import datetime

class AgendaService:
    @staticmethod
    def read_all():
        """Leer todas las agendas disponibles."""
        repository = AgendaRepository()
        return repository.get_all()

    @staticmethod
    def get_by_id(agenda_id):
        """Obtener una agenda por su identificador."""
        repository = AgendaRepository()
        return repository.get_by_id(agenda_id)

    @staticmethod
    def create(agenda: Agenda):
        """Crear y persistir una nueva agenda."""
        repository = AgendaRepository()
        return repository.save(agenda)

    @staticmethod
    def delete(agenda_id):
        """Eliminar una agenda por id; devuelve True si se eliminó."""
        repository = AgendaRepository()
        agenda = repository.get_by_id(agenda_id)
        if agenda:
            repository.delete(agenda)
            return True
        return False
