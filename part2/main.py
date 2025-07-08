from fastapi import FastAPI
from pydantic import BaseModel

class TodoItem(BaseModel):
    title: str
    description: str
    completed: bool
    priority: int

todo_list : list[TodoItem] = []

app = FastAPI()

@app.get("/")
def root():
    return { "message" : "Hello world" }

@app.get("/todos")
def get_todos() -> list[TodoItem]:
    return todo_list

@app.post("/todos")
def add_todo(todo: TodoItem) -> TodoItem:
    todo_list.append(todo)
    return todo

@app.put("/todo/{id}")
def update_todo(id: int, todo: TodoItem) -> TodoItem:
    todo_list[id] = todo
    return todo

@app.delete("/todo/{id}")
def delete_todo(id: int):
    todo_list.pop(id)
    return
