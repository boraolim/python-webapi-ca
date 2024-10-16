import os

class EnvConfig:
    DATABASE_URL_MYSQL = os.getenv("DATABASE_URL_MYSQL")
    DATABASE_URL_MARIA_DB = os.getenv("DATABASE_URL_MARIA_DB")
    SECRET_KEY = os.getenv("API_KEY")
    POOL_SIZE = os.getenv("POOL_SIZE")
    MAX_OVERFLOW = os.getenv("MAX_OVERFLOW")
    POOL_TIMEOUT = os.getenv("POOL_TIMEOUT")
    POOL_RECYCLE = os.getenv("POOL_RECYCLE")
    MAX_NUMBER_CONCURRENT_REQUESTS = os.getenv("MAX_NUMBER_CONCURRENT_REQUESTS")
    MAX_EXECUTION_TIME = os.getenv("MAX_EXECUTION_TIME")
    REQUEST_MAX_NUMBER = os.getenv("REQUEST_MAX_NUMBER")