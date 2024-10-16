from sqlalchemy import text
from sqlalchemy.orm import Session

from app.back.domain.entities.user_entity import UserEntity
from app.back.domain.repository.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):
    def __init__(self, db_session: Session):
        self.uow = db_session

    async def get_by_id(self, user_id: int) -> UserEntity:
        query = await self.uow.execute(text('CALL mydb.proc_get_user(:p_id_user);'),
                                 {'p_id_user': user_id})
        result = query.fetchone()
        return UserEntity(id=result.id, name=result.name, email=result.email,
                          flag_state=result.flag_state, added_at=result.added_at,
                          user_add_date=result.user_add_date, updated_at=result.updated_at,
                          user_update_date=result.user_update_date, deleted_at=result.deleted_at,
                          user_delete_date=result.user_delete_date) if result else None

    async def create(self, user: UserEntity) -> None:
        await self.uow.execute(
            text(
                'CALL mydb.proc_add_new_user(:p_name_user, :p_email_user, :p_created_user_by);'),
            {'p_name_user': user.name, 'p_email_user': user.email,
                'p_created_user_by': 'root'}

        )

    async def delete(self, user_id: int) -> None:
        await self.uow.execute(
            text('DELETE FROM mydb.users WHERE (id = :id);'),
            {'id': user_id}
        )

    async def close(self):
        await self.uow.close()
