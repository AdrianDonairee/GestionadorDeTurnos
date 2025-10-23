from app.repositories.bases_repository import Read
from app import db
from app.models import Agenda

class AgendaRepository(Read, Create, Update):
    
    def get_by_id(self, id: int) -> Agenda:
        return db.session.query(Agenda).filter_by(id=id).first()

    def get_all(self) -> list[Agenda]:
        return db.session.query(Agenda).all()

    def save(self, agenda: Agenda) -> Agenda:
        db.session.add(agenda)
        db.session.commit()
        return agenda

    def update(self, agenda: Agenda) -> Agenda:
        db.session.merge(agenda)
        db.session.commit()
        return agenda


