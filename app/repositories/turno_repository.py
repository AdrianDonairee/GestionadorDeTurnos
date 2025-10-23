from app.models import Turno
from app import db


class TurnoRepository():

    @staticmethod
    def create(turno: Turno) -> Turno:
        if hasattr(turno, "__table__"):
            db.session.add(turno)
            db.session.commit()
            return turno

    @staticmethod
    def get_by_id(id: int) -> Turno:
        if hasattr(Turno, "__table__"):
            return db.session.query(Turno).filter_by(id=id).first()
        return None

    @staticmethod
    def read_all() -> list[Turno]:
        if hasattr(Turno, "__table__"):
            return db.session.query(Turno).all()
        return []

    @staticmethod
    def update(turno: Turno) -> Turno:
        if hasattr(turno, "__table__"):
            db.session.merge(turno)
            db.session.commit()
            return turno

    @staticmethod
    def delete(turno_id: int) -> None:
        if hasattr(Turno, "__table__"):
            turno = db.session.query(Turno).filter_by(id=turno_id).first()
            if turno:
                db.session.delete(turno)
                db.session.commit()
