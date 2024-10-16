from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from app.core.enum.state_enum import StatusRow

class UserDTO(BaseModel):
    id: int
    name: str
    email: str
    flagstate: StatusRow
    createddate: datetime
    usercreatedate: str
    updateddate: Optional[datetime] = Field(default = None)
    userupdatedate: Optional[str] = Field(default = None)
    deletedate: Optional[datetime] = Field(default = None)
    userdeletedate: Optional[str] = Field(default = None)
