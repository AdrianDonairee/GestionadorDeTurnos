from dataclasses import dataclass
from typing import List
from app import db

@dataclass(init=False)
class Agenda(db.Model):
    # Nombre de la tabla
    __tablename__ = "agendas"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Fecha de la agenda
    fecha = db.Column(db.Date, nullable=False)

    recepcionista_id = db.Column(db.Integer, db.ForeignKey('recepcionistas.id'))
    
    # Relación con Recepcionista
    recepcionista = db.relationship("Recepcionista", backref="agendas")
