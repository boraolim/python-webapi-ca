import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger.trace_logger import trace_logger 

class TraceIDMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next):
        trace_id = request.headers.get('x-trace-id', str(uuid.uuid4()))
        request.state.trace_id = trace_id         
        request.state.trace_logger = trace_logger.get_logger(trace_id)
        request.state.trace_logger.info(f"Trace Id detected with value: '{trace_id}'.")
        response = await call_next(request)
        response.headers['x-trace-id'] = trace_id
        return response