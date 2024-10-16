import os

class EnvConfig:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("API_KEY")
    
# Agregar otras variables de entorno aquí.