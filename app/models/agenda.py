from dataclasses import dataclass, field
from typing import List
from app.models.turno import Turno

@dataclass
class Agenda(db.Model):
    __tablename__ = "agendas"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fecha = db.Column(db.Date, nullable=False)
    recepcionista_id = db.Column(db.Integer, nullable=False, db.ForeignKey('recepcionistas.id'))
    
    



    
    turnos: List[Turno] = field(default_factory=list)

    def agregar_turno(self, turno: Turno) -> None:
        """Agrega un turno a la agenda"""
        self.turnos.append(turno)

    def eliminar_turno(self, turno: Turno) -> None:
        """Elimina un turno de la agenda si existe"""
        if turno in self.turnos:
            self.turnos.remove(turno)



