from app.models import Recepcionista
from app import db
from app.repositories import Create, Read

class RecepcionistaRepository(Create, Read):

    @staticmethod
    def create(recepcionista: Recepcionista) -> Recepcionista:
        if hasattr(recepcionista, "__table__"):
            db.session.add(recepcionista)
            db.session.commit()
            return recepcionista

        return recepcionista

    @staticmethod
    def get_by_id(id: int) -> Recepcionista:
        if hasattr(Recepcionista, "__table__"):
            return db.session.query(Recepcionista).filter_by(id=id).first()

        return None

    @staticmethod
    def read_all() -> list[Recepcionista]:
        if hasattr(Recepcionista, "__table__"):
            return db.session.query(Recepcionista).all()

        return []
