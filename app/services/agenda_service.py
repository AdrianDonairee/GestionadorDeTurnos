from app.repositories.agenda_repository import AgendaRepository
from app.models.agenda import Agenda
from datetime import date

class AgendaService:
    def __init__(self):
        self.repository = AgendaRepository()

    
    def listar_agendas():
        return self.repository.get_all()

    
    def obtener_agenda(agenda_id):
        return self.repository.get_by_id(agenda_id)

    
    def crear_agenda(fecha: date):
        nueva_agenda = Agenda(fecha=fecha)
        return self.repository.save(nueva_agenda)

    
    def eliminar_agenda(agenda_id):
        agenda = self.repository.get_by_id(agenda_id)
        if agenda:
            self.repository.delete(agenda)
            return True
        return False
