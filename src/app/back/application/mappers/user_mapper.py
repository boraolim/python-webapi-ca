from datetime import datetime, timezone

from app.core.enum.state_enum import StatusRow
from app.back.application.DTO.user_dto import UserDTO
from app.back.domain.entities.user_entity import UserEntity
from app.back.application.response.user_response import UserResponse
from app.back.application.request.user_request import CreateUserRequest


class UserMapper:

    @staticmethod
    def request_to_dto(request: CreateUserRequest) -> UserDTO:
        return UserDTO(id = 0, name = request.name, email = request.email.lower(), flagstate = StatusRow.ACTIVE,
                       createddate = datetime.now(timezone.utc), usercreatedate = request.author.upper())

    @staticmethod
    def dto_to_entity(dto: UserDTO) -> UserEntity:
        return UserEntity(id = dto.id, name = dto.name, email = dto.email,
                          flag_state = dto.flagstate, added_at = dto.createddate,
                          user_add_date = dto.usercreatedate, updated_at = dto.updateddate,
                          user_update_date = dto.userupdatedate, deleted_at = dto.deletedate,
                          user_delete_date = dto.userdeletedate)

    @staticmethod
    def entity_to_dto(entity: UserEntity) -> UserDTO:
        return UserDTO(id = entity.id, name = entity.name, email = entity.email,
                       flagstate = entity.flag_state, createddate = entity.added_at,
                       usercreatedate = entity.user_add_date, updateddate = entity.updated_at,
                       userupdatedate = entity.user_update_date, userdeletedate = entity.user_delete_date,
                       deletedate = entity.deleted_at)

    @staticmethod
    def dto_to_response(dto: UserDTO) -> UserResponse:
        return UserResponse(id = dto.id, name = dto.name, email = dto.email,
                            flag_state = dto.flagstate, created_date = dto.createddate,
                            user_created_date = dto.usercreatedate, updated_date = dto.updateddate,
                            user_updated_date = dto.userupdatedate, deleted_date = dto.deletedate,
                            user_deleted_date = dto.userdeletedate)
