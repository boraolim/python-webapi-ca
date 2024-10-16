import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger.trace_logger import trace_logger 

class PerformanceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        trace_id = request.headers.get('x-trace-id', str(uuid.uuid4()))
        request.state.trace_logger = trace_logger.get_logger(trace_id)
        
        start_time = time.time()
        response = await call_next(request) 
        process_time = time.time() - start_time
        request.state.trace_logger.info(f"Request to {request.url.path} took {process_time:.4f} seconds")

        if process_time > 1.0:  # Umbral de 1 segundo
            request.state.trace_logger.warning(f"Slow request: {request.url.path} took {process_time:.4f} seconds")
        
        response.headers["X-Process-Time"] = str(process_time)
        return response