from app.models import Paciente
from app.repositories import PacienteRepository

"""Servicio de alto nivel para operaciones sobre pacientes.

Proporciona métodos estáticos que delegan en `PacienteRepository` para
realizar las operaciones CRUD desde la capa de negocio.
"""


class PacienteService:
    @staticmethod
    def read_all():
        """Devuelve todos los pacientes registrados."""
        repository = PacienteRepository()
        return repository.get_all()

    @staticmethod
    def get_by_id(paciente_id):
        """Devuelve el paciente identificado por `paciente_id` o None."""
        repository = PacienteRepository()
        return repository.get_by_id(paciente_id)

    @staticmethod
    def create(paciente: Paciente):
        """Crea y persiste un nuevo `Paciente`. Devuelve la entidad guardada."""
        repository = PacienteRepository()
        return repository.save(paciente)

    @staticmethod
    def delete(paciente_id):
        repository = PacienteRepository()
        paciente = repository.get_by_id(paciente_id)
        if paciente:
            repository.delete(paciente)
            return True
        return False

    @staticmethod
    def update(paciente: Paciente):
        repository = PacienteRepository()
        return repository.update(paciente)
