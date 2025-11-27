from dataclasses import dataclass
from typing import List
from app import db

@dataclass(init=False)
class Agenda(db.Model):
    __tablename__ = "agendas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    fecha = db.Column(db.Date, nullable=False)

    recepcionista_id = db.Column(db.Integer, db.ForeignKey('recepcionistas.id'))
    
    recepcionista = db.relationship("Recepcionista", backref="agendas")
