from app.models import Turno
from app import db
from app.repositories import Read, Update, Delete, Create

"""Repositorio para `Turno`.

Provee operaciones CRUD y devuelve los turnos ordenados por fecha cuando
se solicitan todos los registros. Las operaciones realizan commit al terminar.
"""


class TurnoRepository(Read, Create, Update, Delete):
    def get_by_id(self, id: int) -> Turno:
        """Devuelve el turno con el id indicado o None si no existe."""
        return db.session.query(Turno).filter_by(id=id).first()

    def get_all(self) -> list[Turno]:
        return db.session.query(Turno).order_by(Turno.fecha).all()

    def save(self, turno: Turno) -> Turno:
        """Inserta un nuevo turno y devuelve la entidad persistida."""
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
