from fastapi import FastAPI
from router import todos

app = FastAPI()

app.include_router(
    todos.router,
    prefix="/prefix",
    tags=["todos"]
)