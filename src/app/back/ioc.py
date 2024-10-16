from injector import Binder, singleton

from app.core.environment.environment_config import EnvConfig

from app.back.infrastructure.db.unit_of_work import UnitOfWork
from app.back.infrastructure.db.mysql_context import MySqlContext
from app.back.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

from app.back.application.service.user_service import UserService

def configureioc(binder: Binder):
    db_context = MySqlContext(EnvConfig.DATABASE_URL)
    binder.bind(MySqlContext, to = db_context, scope = singleton)
    binder.bind(UnitOfWork, to = UnitOfWork(db_context), scope = singleton) 
    user_repository = UserRepositoryImpl(db_context.get_session())
    binder.bind(UserRepositoryImpl, to = UserRepositoryImpl(db_context.get_session()), scope = singleton)
    binder.bind(UserService, to = UserService(user_repository), scope = singleton)