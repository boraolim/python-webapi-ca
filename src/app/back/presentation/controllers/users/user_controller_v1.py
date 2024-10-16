from injector import inject
from datetime import datetime
from fastapi import APIRouter, Depends, status, Request, Response

from app.core.result.result_response import Result
from app.core.logger.trace_logger import trace_logger
from app.back.application.mappers.user_mapper import UserMapper
from app.back.application.service.user_service import UserService
from app.back.application.response.user_response import UserResponse
from app.back.application.request.user_request import CreateUserRequest
from app.back.application.dependencies.trace_id_dependency import get_trace_id

class UserController:
    @inject
    def __init__(self, user_service: UserService):
        self.router = APIRouter()
        self.user_service = user_service
        self.router.add_api_route("", self.create_user, methods = ["POST"])
        self.router.add_api_route("/{user_id}", self.delete_user, methods = ["DELETE"])
        self.router.add_api_route("/{user_id}", self.get_user_by_id, methods = ["GET"])

    async def get_user_by_id(self, user_id: int, request: Request, x_trace_id: str = Depends(get_trace_id)) -> Result[UserResponse]:
        try:
            request.state.trace_logger = trace_logger.get_logger(x_trace_id)
            request.state.trace_logger.info(f"Consultando información por el identificador: {user_id}")
            user_dto = await self.user_service.get_user_by_id(user_id)
            request.state.trace_logger.info(f"Información del usuario con el id {user_id} obtenida correctamente.")

            result = Result[UserResponse](
                succeeded = True,
                trace_id = x_trace_id,
                message_description = f"Información del usuario con el id '{user_id}' obtenida correctamente.",
                status_code = status.HTTP_200_OK,
                time_stamp = datetime.now(),
                source_detail = UserMapper.dto_to_response(user_dto),
                url_path_detail = request.url.path,
                method = request.method.upper()
            ).to_json()

            return Response(content = result, media_type = "application/json")
        except Exception as ex:
            request.state.trace_logger.error(f"Ocurrió un error al procesar la solicitud: {str(ex)}")
            raise ex

    async def create_user(self, create_request: CreateUserRequest, request: Request, x_trace_id: str = Depends(get_trace_id)):
        try:
            request.state.trace_logger = trace_logger.get_logger(x_trace_id)
            request.state.trace_logger.info("Guardando...")
            user_create_dto = UserMapper.request_to_dto(create_request)
            await self.user_service.create_user(user_create_dto)
            request.state.trace_logger.info("Información guardada correctamente")
            return Response(status_code = status.HTTP_201_CREATED)
        except Exception as ex:
            request.state.trace_logger.error(f"Ocurrió un error al procesar la solicitud: {str(ex)}")
            raise ex

    async def delete_user(self, user_id: int, request: Request, x_trace_id: str = Depends(get_trace_id)):
        try:
            request.state.trace_logger = trace_logger.get_logger(x_trace_id)
            request.state.trace_logger.info("Eliminando...")
            await self.user_service.delete_user(user_id)
            request.state.trace_logger.info(f"Se ha eliminado el registro con el identicador {user_id} de manera correcta.")
            return Response(status_code = status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            request.state.trace_logger.error(f"Ocurrió un error al procesar la solicitud: {str(ex)}")
            raise ex
