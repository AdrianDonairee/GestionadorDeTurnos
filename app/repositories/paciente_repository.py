from app.repositories import Read, Update, Delete, Create
from app.models import Paciente
from app import db


class PacienteRepository(Read, Create, Update, Delete):
    # Repositorio para la entidad Paciente.
    # Implementa operaciones CRUD sobre la tabla de pacientes usando SQLAlchemy.

    # Devolver el paciente con el id dado, o None si no existe.
    def get_by_id(self, id: int) -> Paciente:
        return db.session.query(Paciente).filter_by(id=id).first()

    # Devolver la lista de todos los pacientes.
    def get_all(self) -> list[Paciente]:
        return db.session.query(Paciente).all()

    # Guardar un nuevo paciente en la base de datos y retornarlo.
    def save(self, paciente: Paciente) -> Paciente:
        db.session.add(paciente)
        db.session.commit()
        return paciente

    # Actualizar los datos de un paciente existente y retornarlo.
    def update(self, paciente: Paciente) -> Paciente:
        db.session.merge(paciente)
        db.session.commit()
        return paciente

    # Eliminar un paciente por su identificador si existe.
    def delete_by_id(self, entity_id: int):
        paciente = self.get_by_id(entity_id)
        if paciente:
            db.session.delete(paciente)
            db.session.commit()

    # Eliminar un paciente dado como instancia.
    def delete(self, entity: Paciente):
        self.delete_by_id(entity.id)
