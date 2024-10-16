from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.environment.environment_config import EnvConfig

class BaseContext(ABC):
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(
                db_url,
                pool_size = int(EnvConfig.POOL_SIZE),         # Tamaño del pool de conexiones
                max_overflow = int(EnvConfig.MAX_OVERFLOW),   # Evitar que el pool crezca sin límite
                pool_timeout = int(EnvConfig.POOL_TIMEOUT),   # Tiempo de espera antes de lanzar un error
                pool_recycle = int(EnvConfig.POOL_RECYCLE),   # Reciclar las conexiones después de 30 min para evitar desconexiones largas
                echo = False,                                 # Deshabilitar logs del SQL por rendimiento
                future = True                                 # Uso de la nueva API de SQLAlchemy
            )
        self.SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = self.engine)
        self.Base = declarative_base()

    @abstractmethod
    def get_session(self):
        pass
