from fastapi import FastAPI
from injector import Injector
from fastapi_injector import attach_injector

from app.back.ioc import configure_ioc
from app.back.presentation.controllers.routes import init_routes
from app.core.middleware.error_handler_middleware import ErrorHandlerMiddleware
from app.back.presentation.middleware.trace_id_middleware import TraceIDMiddleware
from app.back.presentation.middleware.concurrency_limiter import ConcurrencyMiddleware
from app.back.presentation.middleware.performance_middleware import PerformanceMiddleware

class MyFastAPIApp(FastAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.openapi_url = True
        self.docs_url = False
        self.redoc_url = False

        injector = Injector([configure_ioc])
        attach_injector(self, injector)

        self.add_middleware(TraceIDMiddleware)
        self.add_middleware(ConcurrencyMiddleware)
        self.add_middleware(ErrorHandlerMiddleware)
        self.add_middleware(PerformanceMiddleware)

        init_routes(self, injector)
