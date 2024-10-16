from injector import inject

from app.back.application.DTO.user_dto import UserDTO
from app.back.application.mappers.user_mapper import UserMapper
from app.back.domain.repository.user_repository import UserRepository
from app.core.exceptions.entity_not_found_exception import EntityNotFoundException

class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_user_by_id(self, user_id: int) -> UserDTO:
        user = await self.user_repository.get_by_id(user_id)

        if user is None:
            raise EntityNotFoundException(f"No se encontró ningun usuario con el identificador '{user_id}'", 1001)

        return UserMapper.entity_to_dto(user)

    async def create_user(self, user_create_dto: UserDTO) -> None:
        await self.user_repository.create(UserMapper.dto_to_entity(user_create_dto))

    async def delete_user(self, user_id: int) -> None:
        await self.user_repository.delete(user_id)
