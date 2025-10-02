from app.models.paciente import Paciente
from app.repositories.paciente_repository import PacienteRepository

class PacienteService:
    def __init__(self, repository: PacienteRepository):
        self.repository = repository

    def registrar_paciente(self, nombre, apellido, dni, email, fechadenacimiento, telefono):
        paciente = Paciente(
            nombre=nombre,
            apellido=apellido,
            dni=dni,
            email=email,
            fechadenacimiento=fechadenacimiento,
            telefono=telefono
        )
        paciente_id, paciente_guardado = self.repository.save(paciente)
        return paciente_id, paciente_guardado

    def obtener_paciente(self, paciente_id: int):
        return self.repository.get_by_id(paciente_id)
