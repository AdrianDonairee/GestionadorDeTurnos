from dataclasses import dataclass
from app import db

"""Modelo `Turno`.

Representa una cita con fecha y estado; enlaza opcionalmente con un
`Paciente` y una `Agenda`. Se utiliza para reservar y cancelar turnos.
"""

@dataclass
class Turno(db.Model):
    __tablename__ = 'turnos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(20), default="disponible")
    paciente_id = db.Column('paciente_id', db.Integer, db.ForeignKey('pacientes.id'))
    agenda_id = db.Column('agenda_id', db.Integer, db.ForeignKey('agendas.id'))
    paciente = db.relationship("Paciente", backref="turnos")
    agenda = db.relationship("Agenda", backref="turnos")
    

    