from fastapi import APIRouter
from pydantic import BaseModel

class TodoItem(BaseModel):
    title: str
    description: str
    completed: bool
    priority: int

router = APIRouter()

todo_list : list[TodoItem] = []

@router.get("/")
def root():
    return { "message" : "Hello world" }

@router.get("/todos")
def get_todos() -> list[TodoItem]:
    return todo_list

@router.post("/todos")
def add_todo(todo: TodoItem) -> TodoItem:
    todo_list.append(todo)
    return todo

@router.put("/todo/{id}")
def update_todo(id: int, todo: TodoItem) -> TodoItem:
    todo_list[id] = todo
    return todo

@router.delete("/todo/{id}")
def delete_todo(id: int):
    todo_list.pop(id)
    return

@router.get("/todo/{id}")
def get_todo(id: int) -> TodoItem:
    return todo_list[id]