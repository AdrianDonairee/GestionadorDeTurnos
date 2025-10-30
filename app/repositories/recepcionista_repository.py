from app.models.recepcionista import Recepcionista
from app.repositories import Read, Update, Delete, Create
from app import db

class RecepcionistaRepository(Read, Create, Update, Delete):
    def get_by_id(self, id: int) -> Recepcionista:
        return db.session.query(Recepcionista).filter_by(id=id).first()

    def get_all(self) -> list[Recepcionista]:
        return db.session.query(Recepcionista).all()

    def save(self, recepcionista: Recepcionista) -> Recepcionista:
        db.session.add(recepcionista)
        db.session.commit()
        return recepcionista

    def update(self, recepcionista: Recepcionista) -> Recepcionista:
        db.session.merge(recepcionista)
        db.session.commit()
        return recepcionista

    def delete_by_id(self, entity_id: int):
        recepcionista = self.get_by_id(entity_id)
        if recepcionista:
            db.session.delete(recepcionista)
            db.session.commit()

    def delete(self, entity: Recepcionista):
        self.delete_by_id(entity.id)
