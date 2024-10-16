from abc import ABC, abstractmethod
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

class BaseContext(ABC):
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_async_engine(self.db_url)
        self.SessionLocal = sessionmaker(bind = self.engine, class_ = AsyncSession, expire_on_commit = False)
        self.Base = declarative_base()

    @abstractmethod
    def get_session(self):
        pass
