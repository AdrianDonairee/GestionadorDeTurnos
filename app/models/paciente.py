from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Paciente(db.Model):
    # Modelo Paciente.
    # Atributos:
    # - id: identificador único del paciente
    # - nombre, apellido, dni, email, fechadenacimiento, telefono
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(30), nullable=False)
    apellido: str = db.Column(db.String(30), nullable=False)
    dni: str = db.Column(db.String(10), nullable=False)
    email: str = db.Column(db.String(150), nullable=False)
    fechadenacimiento = db.Column(db.Date, nullable=False)
    telefono: str = db.Column(db.String(20), nullable=False)
    