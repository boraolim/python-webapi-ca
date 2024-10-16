from enum import Enum

class StatusRow(Enum):
    ACTIVE = (1, "ACTIVE")
    LOCKED = (2, "LOCKED")
    DELETED = (3, "DELETED")
    
    def __init__(self, code, caption):
        self.code = code
        self.caption = caption
        
    @classmethod
    def is_valid_caption(cls, caption: str) -> bool:
        return any(caption == status.caption for status in cls)

    @classmethod
    def get_by_caption(cls, value: str):
        for status in cls:
            if value in (status.caption, status.code):
                return status
        raise ValueError(f"El valor '{value}' no es una opción válida.")