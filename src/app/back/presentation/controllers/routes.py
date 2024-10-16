from fastapi import FastAPI
from injector import Injector

from app.back.presentation.controllers.users.user_controller_v1 import UserController

def init_routes(app: FastAPI, injector: Injector):
    user_controlller = injector.get(UserController)
    app.include_router(user_controlller.router, prefix = "/api/v1/users", tags = ["Usuarios"])