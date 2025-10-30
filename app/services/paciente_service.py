from app.models import Paciente
from app.repositories import PacienteRepository

class PacienteService:
    @staticmethod
    def read_all():
        repository = PacienteRepository()
        return repository.get_all()

    @staticmethod
    def get_by_id(paciente_id):
        repository = PacienteRepository()
        return repository.get_by_id(paciente_id)
    @staticmethod
    def create(paciente:Paciente):
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
