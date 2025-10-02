from app.models.recepcionista import Recepcionista
from app.repositories.recepcionista_repository import RecepcionistaRepository

class RecepcionistaService:
    def __init__(self, repository: RecepcionistaRepository):
        self.repository = repository

    def registrar_recepcionista(self, nombre, email):
        recepcionista = Recepcionista(nombre, email)
        recepcionista_id, recepcionista_guardado = self.repository.save(recepcionista)
        return recepcionista_id, recepcionista_guardado

    def obtener_recepcionista(self, recepcionista_id):
        return self.repository.get_by_id(recepcionista_id)
