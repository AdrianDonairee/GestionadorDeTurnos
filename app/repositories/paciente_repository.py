from app.repositories import Read, Update, Delete, Create
from app.models import Paciente
from app import db


class PacienteRepository(Read, Create, Update, Delete):

    def get_by_id(self, id: int) -> Paciente:
        return db.session.query(Paciente).filter_by(id=id).first()

    def get_all(self) -> list[Paciente]:
        return db.session.query(Paciente).all()

    def save(self, paciente: Paciente) -> Paciente:
        db.session.add(paciente)
        db.session.commit()
        return paciente

    def update(self, paciente: Paciente) -> Paciente:
        db.session.merge(paciente)
        db.session.commit()
        return paciente

    def delete_by_id(self, entity_id: int):
        paciente = self.get_by_id(entity_id)
        if paciente:
            db.session.delete(paciente)
            db.session.commit()

    def delete(self, entity: Paciente):
        self.delete_by_id(entity.id)
