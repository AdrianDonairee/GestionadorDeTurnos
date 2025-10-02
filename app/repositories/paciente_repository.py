from app.models.paciente import Paciente
from .create import Create
from .read import Read

class PacienteRepository:
    def __init__(self):
        self._pacientes = {}
        self._next_id = 1

    def save(self, paciente: Paciente):
        paciente_id = self._next_id
        self._pacientes[paciente_id] = paciente
        self._next_id += 1
        return paciente_id, paciente

    def get_by_id(self, paciente_id: int):
        return self._pacientes.get(paciente_id)

    def get_all(self):
        return self._pacientes.items()
