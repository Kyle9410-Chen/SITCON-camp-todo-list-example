from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class TodoItem(BaseModel):
    title: str
    description: str
    completed: bool
    priority: int = Field(gt = 0)

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
    if id < 0 or id >= len(todo_list):
        raise HTTPException(
            status_code=404,
            detail="Todo item not found"
            )
    todo_list[id] = todo
    return todo

@app.delete("/todo/{id}")
def delete_todo(id: int):
    if id < 0 or id >= len(todo_list):
        raise HTTPException(
            status_code=404,
            detail="Todo item not found"
            )
    todo_list.pop(id)
    return

@app.get("/todo/{id}")
def get_todo(id: int) -> TodoItem:
    if id < 0 or id >= len(todo_list):
        raise HTTPException(
            status_code=404,
            detail="Todo item not found"
            )
    return todo_list[id]