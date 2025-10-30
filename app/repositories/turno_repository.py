from app.models import Turno
from app import db
from app.repositories import Read, Update, Delete, Create


class TurnoRepository(Read, Create, Update, Delete):

    def get_by_id(self, id: int) -> Turno:
        return db.session.query(Turno).filter_by(id=id).first()

    def get_all(self) -> list[Turno]:
        return db.session.query(Turno).all()

    def save(self, turno: Turno) -> Turno:
        db.session.add(turno)
        db.session.commit()
        return turno

    def update(self, turno: Turno) -> Turno:
        db.session.merge(turno)
        db.session.commit()
        return turno

    def delete_by_id(self, entity_id: int):
        turno = self.get_by_id(entity_id)
        if turno:
            db.session.delete(turno)
            db.session.commit()

    def delete(self, entity: Turno):
        self.delete_by_id(entity.id)
