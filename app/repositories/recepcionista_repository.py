from app.models.recepcionista import Recepcionista

class RecepcionistaRepository:
    def __init__(self):
        self._recepcionistas = {}
        self._next_id = 1

    def save(self, recepcionista: Recepcionista):
        recepcionista_id = self._next_id
        self._recepcionistas[recepcionista_id] = recepcionista
        self._next_id += 1
        return recepcionista_id, recepcionista

    def get_by_id(self, recepcionista_id: int):
        return self._recepcionistas.get(recepcionista_id)

    def get_all(self):
        return self._recepcionistas.items()
