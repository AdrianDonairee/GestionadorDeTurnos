from dataclasses import dataclass, field
from typing import List
from app.models.turno import Turno

@dataclass
class Agenda:
    recepcionista_id: int
    turnos: List[Turno] = field(default_factory=list)

    def agregar_turno(self, turno: Turno) -> None:
        """Agrega un turno a la agenda"""
        self.turnos.append(turno)

    def eliminar_turno(self, turno: Turno) -> None:
        """Elimina un turno de la agenda si existe"""
        if turno in self.turnos:
            self.turnos.remove(turno)
