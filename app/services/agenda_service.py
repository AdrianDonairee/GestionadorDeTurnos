from app.repositories.agenda_repository import AgendaRepository
from app.models.agenda import Agenda
from datetime import date

class AgendaService:

    @staticmethod
    def listar_agendas():
        return AgendaRepository.get_all()

    @staticmethod
    def obtener_agenda(agenda_id):
        return AgendaRepository.get_by_id(agenda_id)

    @staticmethod
    def crear_agenda(fecha: date):
        nueva_agenda = Agenda(fecha=fecha)
        return AgendaRepository.save(nueva_agenda)

    @staticmethod
    def eliminar_agenda(agenda_id):
        agenda = AgendaRepository.get_by_id(agenda_id)
        if agenda:
            AgendaRepository.delete(agenda)
            return True
        return False
