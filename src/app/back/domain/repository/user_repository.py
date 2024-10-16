from abc import ABC, abstractmethod
from app.back.domain.entities.user_entity import UserEntity

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> UserEntity:
        pass

    @abstractmethod
    def create(self, user: UserEntity) -> None:
        pass
    
    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass