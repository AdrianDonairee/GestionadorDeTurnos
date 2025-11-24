from app.models import Recepcionista
from app.repositories import RecepcionistaRepository

class RecepcionistaService:
    """Servicio con operaciones CRUD para la entidad `Recepcionista`.

    Se delega la persistencia en `RecepcionistaRepository` y se mantiene
    la lógica de negocio mínima en este servicio."""

    @staticmethod
    def read_all():
        """Devolver la lista de todas las recepcionistas."""
        repository = RecepcionistaRepository()
        return repository.get_all()

    @staticmethod
    def get_by_id(recepcionista_id):
        """Obtener una recepcionista por su identificador."""
        repository = RecepcionistaRepository()
        return repository.get_by_id(recepcionista_id)

    @staticmethod
    def create(recepcionista: Recepcionista):
        """Crear y persistir una nueva recepcionista."""
        repository = RecepcionistaRepository()
        return repository.save(recepcionista)

    @staticmethod
    def delete(recepcionista_id):
        """Eliminar la recepcionista con el id dado. Devuelve True si se
        eliminó, False si no existía."""
        repository = RecepcionistaRepository()
        recepcionista = repository.get_by_id(recepcionista_id)
        if recepcionista:
            repository.delete(recepcionista)
            return True
        return False

    @staticmethod
    def update(recepcionista: Recepcionista):
        """Actualizar una recepcionista existente y persistir cambios."""
        repository = RecepcionistaRepository()
        return repository.update(recepcionista)
