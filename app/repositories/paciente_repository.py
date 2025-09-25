from app.models import Paciente
from app import db
from typing import List
from app.repositories import Create, Read, Update, Delete

class PacienteRepository(Create, Read, Update, Delete): 

    @staticmethod
    def create(paciente: Paciente) -> Paciente:
        db.session.add(paciente)
        db.session.commit()
        return paciente

    @staticmethod
    def get_by_id(id: int) -> Paciente:
        return db.session.query(Paciente).filter_by(id=id).first()
    
    @staticmethod
    def read_all() -> list[Paciente]:
        return db.session.query(Paciente).all()
    
    @staticmethod
    def update(paciente: Paciente) -> Paciente:
        db.session.merge(paciente)
        db.session.commit()
        return paciente
    
    @staticmethod
    def delete(paciente: Paciente) -> None:
        db.session.delete(paciente)
        db.session.commit()
