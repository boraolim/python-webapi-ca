from contextlib import contextmanager

from app.back.infrastructure.db.base_context import BaseContext

class UnitOfWork:
    def __init__(self, db_context: BaseContext):
        self.db = db_context.get_session()
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.db.rollback()
        else:
            self.db.commit()
        self.db.close()
        
    @contextmanager
    def transactional(self):
        try:
            yield self.db
            self.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        finally:
            self.close()