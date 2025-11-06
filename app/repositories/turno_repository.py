from app.models import Turno
from app import db
from app.repositories import Read, Update, Delete, Create


class TurnoRepository(Read, Create, Update, Delete):
    # Repositorio para la entidad Turno.
    # Implementa operaciones CRUD sobre la tabla de turnos usando SQLAlchemy.

    # Devolver el turno con el id dado, o None si no existe.
    def get_by_id(self, id: int) -> Turno:
        return db.session.query(Turno).filter_by(id=id).first()

    # Devolver la lista de todos los turnos.
    def get_all(self) -> list[Turno]:
        return db.session.query(Turno).all()

    # Guardar un nuevo turno y retornarlo.
    def save(self, turno: Turno) -> Turno:
        db.session.add(turno)
        db.session.commit()
        return turno

    # Actualizar un turno existente y retornarlo.
    def update(self, turno: Turno) -> Turno:
        db.session.merge(turno)
        db.session.commit()
        return turno

    # Eliminar un turno por su identificador si existe.
    def delete_by_id(self, entity_id: int):
        turno = self.get_by_id(entity_id)
        if turno:
            db.session.delete(turno)
            db.session.commit()

    # Eliminar un turno dado como instancia.
    def delete(self, entity: Turno):
        self.delete_by_id(entity.id)
