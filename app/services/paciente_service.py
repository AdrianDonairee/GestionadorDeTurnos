from app.models import Paciente
from app.repositories import PacienteRepository

class PacienteService:
    # Servicio de alto nivel para operaciones sobre Paciente.
    # Provee métodos estáticos que delegan en el repositorio.

    @staticmethod
    # Devolver todos los pacientes
    def read_all():
        repository = PacienteRepository()
        return repository.get_all()

    @staticmethod
    # Devolver un paciente por su id
    def get_by_id(paciente_id):
        repository = PacienteRepository()
        return repository.get_by_id(paciente_id)

    @staticmethod
    def create(paciente: Paciente):
        """Crear (persistir) un nuevo paciente.

        Args:
            paciente (Paciente): Instancia de `Paciente` a guardar en el repositorio.

        Returns:
            Paciente: La entidad `Paciente` guardada (normalmente con el id asignado)
            o el valor que devuelva el repositorio en caso de fallo.
        """
        repository = PacienteRepository()
        return repository.save(paciente)

    @staticmethod
    # Eliminar un paciente por id (devuelve True si se eliminó)
    def delete(paciente_id):
        repository = PacienteRepository()
        paciente = repository.get_by_id(paciente_id)
        if paciente:
            repository.delete(paciente)
            return True
        return False

    @staticmethod
    # Actualizar un paciente existente
    def update(paciente: Paciente):
        repository = PacienteRepository()
        return repository.update(paciente)
