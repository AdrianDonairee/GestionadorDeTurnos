from app.repositories import AgendaRepository
from app.models import Agenda
from datetime import date

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
    def create(fecha: date):
        repository = AgendaRepository()
        nueva_agenda = Agenda(fecha=fecha)
        return repository.save(nueva_agenda)

    @staticmethod
    def delete(agenda_id):
        repository = AgendaRepository()
        agenda = repository.get_by_id(agenda_id)
        if agenda:
            repository.delete(agenda)
            return True
        return False
