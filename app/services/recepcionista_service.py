from app.models import Recepcionista
from app.repositories import RecepcionistaRepository

class RecepcionistaService:
    @staticmethod
    def read_all():
        repository = RecepcionistaRepository()
        return repository.get_all()

    @staticmethod
    def get_by_id(recepcionista_id):
        repository = RecepcionistaRepository()
        return repository.get_by_id(recepcionista_id)

    @staticmethod
    def create(recepcionista: Recepcionista):
        repository = RecepcionistaRepository()
        
        return repository.save(recepcionista)

    @staticmethod
    def delete(recepcionista_id):
        repository = RecepcionistaRepository()
        recepcionista = repository.get_by_id(recepcionista_id)
        if recepcionista:
            repository.delete(recepcionista)
            return True
        return False

    @staticmethod
    def update(recepcionista: Recepcionista):
        repository = RecepcionistaRepository()
        return repository.update(recepcionista)
