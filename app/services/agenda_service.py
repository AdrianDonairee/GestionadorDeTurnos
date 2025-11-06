from app.repositories import AgendaRepository
from app.models import Agenda
from datetime import datetime

class AgendaService:

    @staticmethod
    # Leer todas las agendas
    def read_all():
        repository = AgendaRepository()
        return repository.get_all()

    @staticmethod
    # Obtener una agenda por su id
    def get_by_id(agenda_id):
        repository = AgendaRepository()
        return repository.get_by_id(agenda_id)

    @staticmethod
    # Crear una nueva agenda
    def create(agenda: Agenda):
        repository = AgendaRepository()
        return repository.save(agenda)

    @staticmethod
    # Eliminar una agenda por id
    def delete(agenda_id):
        repository = AgendaRepository()
        agenda = repository.get_by_id(agenda_id)
        if agenda:
            repository.delete(agenda)
            return True
        return False
