from dataclasses import dataclass
from datetime import date, time

@dataclass
class Turno:
    fecha: date
    hora: time
    estado: str = "disponible"
    paciente_id: int | None = None   # opcional, por si más adelante querés asociarlo

    def asignar_cliente(self):
        """Marca el turno como reservado"""
        self.estado = "reservado"

    def liberar_turno(self):
        """Libera el turno y lo deja disponible"""
        self.estado = "disponible"
