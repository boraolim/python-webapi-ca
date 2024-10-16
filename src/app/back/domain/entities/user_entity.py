from pydantic import Field
from typing import Optional
from datetime import datetime

from app.core.enum.state_enum import StatusRow
from app.core.entity.base_entity import BaseEntity

class UserEntity(BaseEntity[int]):
    name: str
    email: str