import orjson

from pydantic import Field
from datetime import datetime
from fastapi_camelcase import CamelModel
from typing import Generic, TypeVar, Optional, Dict

T = TypeVar('T')

class Result(CamelModel, Generic[T]):
    succeeded: bool = Field(default = False)
    trace_id: str = Field(default = "")
    message_description: str = Field(default = "")
    status_code: int = Field(default = 0)
    time_stamp: Optional[datetime] = Field(default = None)
    error_detail: Optional[Dict[str, str]] = Field(default = None)
    source_detail: Optional[T] = Field(default = None)
    url_path_detail: str = Field(default = "")
    method: str = Field(default = None) 
    
    def to_json(self):
        return orjson.dumps(
            self.model_dump(exclude_none = True, by_alias = True), 
            option = orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_INDENT_2 | orjson.OPT_PASSTHROUGH_DATACLASS ).decode("utf-8")
