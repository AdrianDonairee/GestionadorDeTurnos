from app import db
from app.models.turno import Turno

class Agenda(db.Model):
    __tablename__ = "agendas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    turnos = db.relationship("Turno", backref="agenda", lazy=True)

    def __init__(self, fecha):
        self.fecha = fecha

    def __repr__(self):
        return f"<Agenda {self.fecha}>"

