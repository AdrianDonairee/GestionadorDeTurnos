from app.models.agenda import Agenda

class AgendaRepository:
    def __init__(self):
        self.agendas = []

    def add_agenda(self, agenda_data: dict) -> Agenda:
        agenda = Agenda(**agenda_data)
        self.agendas.append(agenda)
        return agenda

    def get_agenda(self, recepcionista_id: int) -> Agenda | None:
        for agenda in self.agendas:
            if agenda.recepcionista_id == recepcionista_id:
                return agenda
        return None

    def list_agendas(self) -> list[Agenda]:
        return self.agendas.copy()

    def delete_agenda(self, recepcionista_id: int) -> bool:
        agenda = self.get_agenda(recepcionista_id)
        if agenda:
            self.agendas.remove(agenda)
            return True
        return False

    def update_agenda(self, recepcionista_id: int, update_data: dict) -> Agenda | None:
        agenda = self.get_agenda(recepcionista_id)
        if agenda:
            for key, value in update_data.items():
                setattr(agenda, key, value)
            return agenda
        return None
