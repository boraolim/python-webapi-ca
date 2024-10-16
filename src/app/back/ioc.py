from injector import Binder, singleton

from app.core.environment.environment_config import EnvConfig

from app.back.infrastructure.db.unit_of_work import UnitOfWork
from app.back.infrastructure.db.mariadb_context import MariaDbContext
from app.back.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

from app.back.application.service.user_service import UserService

def configure_ioc(binder: Binder):
    db_context_maria_db = MariaDbContext(EnvConfig.DATABASE_URL_MARIA_DB)
    binder.bind(MariaDbContext, to = db_context_maria_db, scope = singleton)
    binder.bind(UnitOfWork, to = UnitOfWork(db_context_maria_db), scope = singleton)
    user_repository = UserRepositoryImpl(db_context_maria_db.get_session())
    binder.bind(UserRepositoryImpl, to = UserRepositoryImpl(db_context_maria_db.get_session()), scope = singleton)
    binder.bind(UserService, to = UserService(user_repository), scope = singleton)
