from pydantic import Field
from datetime import datetime
from typing import Optional
from fastapi_camelcase import CamelModel

from app.core.enum.state_enum import StatusRow

class UserResponse(CamelModel):
    id: int
    name: str
    email: str
    flag_state: StatusRow
    created_date: Optional[datetime] = Field(default = None)
    user_created_date: Optional[str] = Field(default = None)
    updated_date: Optional[datetime] = Field(default = None)
    user_updated_date: Optional[str] = Field(default = None)
    deleted_date: Optional[datetime] = Field(default = None)
    user_deleted_date: Optional[str] = Field(default = None)