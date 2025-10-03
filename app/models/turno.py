from app import db
from datetime import date, time

class Turno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(20), default="disponible")
    paciente_id = db.Column(db.Integer, nullable=True)

    def asignar_cliente(self):
        self.estado = "reservado"

    def liberar_turno(self):
        self.estado = "disponible"