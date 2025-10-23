from abc import ABC, abstractmethod

class Read(ABC):
    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

class Create(ABC):
    @abstractmethod
    def save(self, entity):
        pass

class Update(ABC):
    @abstractmethod
    def update(self, entity):
        pass

class Delete(ABC):
    @abstractmethod
    def delete_by_id(self, entity_id: int):
        pass
    @abstractmethod
    def delete(self, entity):
        self.delete_by_id(entity.id)
