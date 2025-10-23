from .venv.Lib.site-packages.sqlalchemy.testing.provision import get_temp_table_name
from dataclasses import dataclass
from app import db
from datetime import date, time

@dataclass
class Turno(db.Model):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(20), default="disponible")
    paciente_id = db.Column(db.Integer, nullable=True, db.ForeignKey('pacientes.id'))
    agenda_id = db.Column(db.Integer, nullable=False, db.ForeignKey('agendas.id'))
    paciente = db.relationship("Paciente", backref="turnos")
    agenda = db.relationship("Agenda", backref="turnos")
    

    def asignar_cliente(self):
        self.estado = "reservado"

    def liberar_turno(self):
        self.estado = "disponible"