from abc import ABC, abstractmethod


class Read(ABC):
    # Interfaz para operaciones de lectura en un repositorio.
    # Métodos a implementar:
    # - get_by_id(id): obtener entidad por id
    # - get_all(): obtener todas las entidades
    @abstractmethod
    def get_by_id(self, id: int):
        pass
        # Obtener una entidad por su identificador.

    @abstractmethod
    def get_all(self):
        # Obtener todas las entidades del repositorio.
        pass


class Create(ABC):
    # Interfaz para operaciones de creación en un repositorio.
    @abstractmethod
    def save(self, entity):
        # Guardar una nueva entidad en el repositorio.
        pass


class Update(ABC):
    # Interfaz para operaciones de actualización en un repositorio.
    @abstractmethod
    def update(self, entity):
        # Actualizar una entidad existente.
        pass


class Delete(ABC):
    # Interfaz para operaciones de borrado en un repositorio.
    @abstractmethod
    def delete_by_id(self, entity_id: int):
        # Eliminar una entidad dado su identificador.
        pass

    @abstractmethod
    def delete(self, entity):
        # Eliminar una entidad pasada como instancia.
        # Implementación por defecto: eliminar por id.
        self.delete_by_id(entity.id)
