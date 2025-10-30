from app.repositories import AgendaRepository
from app.models import Agenda
from datetime import datetime

class AgendaService:

    @staticmethod
    def read_all():
        repository = AgendaRepository()
        return repository.get_all()

    @staticmethod
    def get_by_id(agenda_id):
        repository = AgendaRepository()
        return repository.get_by_id(agenda_id)

    @staticmethod
    def create(agenda: Agenda):
        repository = AgendaRepository()
        return repository.save(agenda)

    @staticmethod
    def delete(agenda_id):
        repository = AgendaRepository()
        agenda = repository.get_by_id(agenda_id)
        if agenda:
            repository.delete(agenda)
            return True
        return False
