from app.repositories import Read, Create, Update
from app import db
from app.models import Agenda


class AgendaRepository(Read, Create, Update):
    # Repositorio para la entidad Agenda.

    # Devolver la agenda con el id dado, o None si no existe.
    def get_by_id(self, id: int) -> Agenda:
        return db.session.query(Agenda).filter_by(id=id).first()

    # Devolver la lista de todas las agendas.
    def get_all(self) -> list[Agenda]:
        return db.session.query(Agenda).all()

    # Guardar una nueva agenda y retornarla.
    def save(self, agenda: Agenda) -> Agenda:
        db.session.add(agenda)
        db.session.commit()
        return agenda

    # Actualizar una agenda existente y retornarla.
    def update(self, agenda: Agenda) -> Agenda:
        db.session.merge(agenda)
        db.session.commit()
        return agenda


