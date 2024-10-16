import uuid

from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.result.result_response import Result
from app.core.exceptions.entity_not_found_exception import EntityNotFoundException
from app.core.exceptions.concurrency_exception import ConcurrencyException

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        result = Result[str](
            trace_id = request.headers.get('x-trace-id', str(uuid.uuid4())),
            url_path_detail = request.url.path,
            method = request.method.upper(),
            time_stamp = datetime.now()
        )

        try:
            response = await call_next(request)
            return response
        except SQLAlchemyError as e:
            request.state.trace_logger.error(f"SQL Error: {str(e)}")
            result.message_description = "Error al realizar la operación en Base de Datos."
            result.error_detail = { "SQLError": str(e) }
            result.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        except ConcurrencyException as e:
            request.state.trace_logger.error(f"Ocurrió un error al procesar esta solicitud: {str(e)}")
            result.message_description = "Ocurrio un error al procesar esta solicitud. Revise los detalles."
            result.error_detail = { "UNAVAILABLE": f"Servicio no disponible por concurrencia excedida por los límites del servidor. Detalle: {str(e)}" }
            result.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        except EntityNotFoundException as e:
            request.state.trace_logger.error(f"Ocurrió un error al procesar esta solicitud: {str(e)}")
            result.message_description = "Ocurrio un error al procesar esta solicitud. Revise los detalles."
            result.error_detail = { "NOTFOUND": f"Recurso no encontrado. Detalle: {str(e)}" }
            result.status_code = status.HTTP_404_NOT_FOUND
        except Exception as e:
            request.state.trace_logger.error(f"Ocurrió un error al procesar esta solicitud: {str(e)}")
            result.message_description = "Ocurrio un error al procesar esta solicitud. Revise los detalles."

            if isinstance(e, ValueError):
                result.error_detail = { "NOTVALID": f"Valor no válido. Detalle: {str(e)}" }
                result.status_code = status.HTTP_400_BAD_REQUEST
            elif isinstance(e, KeyError):
                result.error_detail = { "KEYNOTFOUND": f"Clave no encontrada. Detalle: {str(e)}" }
                result.status_code = status.HTTP_404_NOT_FOUND
            else:
                result.error_detail = { "INTERNALERR": f"Error interno en el servidor. Detalle: {str(e)}" }
                result.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        result_json = result.to_json()
        return Response(content = result_json, status_code = result.status_code, media_type = "application/json")
