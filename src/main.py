import uvicorn

from my_fast_api import MyFastAPIApp

app = MyFastAPIApp()

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000, log_level = "info")