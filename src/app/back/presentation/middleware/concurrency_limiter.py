import uuid
import asyncio

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger.trace_logger import trace_logger
from app.core.environment.environment_config import EnvConfig
from app.core.exceptions.concurrency_exception import ConcurrencyException

semaphore = asyncio.Semaphore(int(EnvConfig.MAX_NUMBER_CONCURRENT_REQUESTS))

class ConcurrencyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, timeout: float = float(EnvConfig.MAX_EXECUTION_TIME)):
        super().__init__(app)
        self.timeout = timeout

    async def dispatch(self, request: Request, call_next):
        trace_id = request.headers.get('x-trace-id', str(uuid.uuid4()))
        request.state.trace_logger = trace_logger.get_logger(trace_id)

        try:
            acquired = await asyncio.wait_for(semaphore.acquire(), timeout = self.timeout)

            if acquired:
                response = await call_next(request)
        except asyncio.TimeoutError:
            raise ConcurrencyException("Concurrencia superada por el límite máximo de peticiones soportadas por el servidor.", 1002)
        finally:
            if semaphore.locked():
                semaphore.release()

        return response
