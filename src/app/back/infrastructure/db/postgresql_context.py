from app.back.infrastructure.db.base_context import BaseContext

class PostgreSQLContext(BaseContext):
    def __init__(self, db_url: str):
        super().__init__(db_url)
                         
    def get_session(self):
        return self.SessionLocal()