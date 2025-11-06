from app.models import Recepcionista
from app.repositories import RecepcionistaRepository

class RecepcionistaService:
    # Servicio para operaciones sobre Recepcionista
    @staticmethod
    # Devolver todos los recepcionistas
    def read_all():
        repository = RecepcionistaRepository()
        return repository.get_all()

    @staticmethod
    # Obtener recepcionista por id
    def get_by_id(recepcionista_id):
        repository = RecepcionistaRepository()
        return repository.get_by_id(recepcionista_id)

    @staticmethod
    # Crear una nueva recepcionista
    def create(recepcionista: Recepcionista):
        repository = RecepcionistaRepository()
        return repository.save(recepcionista)

    @staticmethod
    # Eliminar recepcionista por id
    def delete(recepcionista_id):
        repository = RecepcionistaRepository()
        recepcionista = repository.get_by_id(recepcionista_id)
        if recepcionista:
            repository.delete(recepcionista)
            return True
        return False

    @staticmethod
    # Actualizar recepcionista existente
    def update(recepcionista: Recepcionista):
        repository = RecepcionistaRepository()
        return repository.update(recepcionista)
