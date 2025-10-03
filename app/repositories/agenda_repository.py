from app import db
from app.models.agenda import Agenda

class AgendaRepository:

    @staticmethod
    def get_all():
        return Agenda.query.all()

    @staticmethod
    def get_by_id(agenda_id):
        return Agenda.query.get(agenda_id)

    @staticmethod
    def save(agenda):
        db.session.add(agenda)
        db.session.commit()
        return agenda

    @staticmethod
    def delete(agenda):
        db.session.delete(agenda)
        db.session.commit()
