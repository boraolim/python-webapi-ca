from datetime import datetime
from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, Field, field_validator

from app.core.enum.state_enum import StatusRow

T = TypeVar('T')

class BaseEntity(BaseModel, Generic[T]):
    id: T
    flag_state: StatusRow
    added_at: datetime
    user_add_date: str
    updated_at: Optional[datetime] = Field(default = None)
    user_update_date: Optional[str] = Field(default = None)
    deleted_at: Optional[datetime] = Field(default = None)
    user_delete_date: Optional[str] = Field(default = None)

    @field_validator('flag_state', mode='before')
    def validate_flagstate(cls, value):
        if isinstance(value, StatusRow):
            return value
        return StatusRow.get_by_caption(value)
