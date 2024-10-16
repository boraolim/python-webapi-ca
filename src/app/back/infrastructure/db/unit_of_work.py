from contextlib import contextmanager

from app.back.infrastructure.db.base_context import BaseContext

class UnitOfWork:
    def __init__(self, db_context: BaseContext):
        self.db = db_context.get_session()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.db.rollback()
        else:
            await self.db.commit()
        await self.db.close()

    @contextmanager
    async def transactional(self):
        try:
            yield self.db
            await self.commit()
        except Exception as e:
            await self.db.rollback()
            raise e
        finally:
            await self.close()
