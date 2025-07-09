from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import json

class TodoItem(BaseModel):
    title: str
    description: str
    completed: bool
    priority: int = Field(gt = 0)

todo_list : list[TodoItem] = []

app = FastAPI()

def load_data():
    global todo_list
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            for item in data:
                todo_list.append(TodoItem(**item))
        return todo_list
    except:
        return []

def save_data():
    try:
        data = []
        with open("data.json", "w") as f:
            for item in todo_list:
                data.append(item.dict())
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)


@app.get("/")
def root():
    return { "message" : "Hello world" }

@app.get("/todos")
def get_todos() -> list[TodoItem]:
    return load_data()

@app.post("/todos")
def add_todo(todo: TodoItem) -> TodoItem:
    load_data()
    todo_list.append(todo)
    save_data()
    return todo

@app.put("/todo/{id}")
def update_todo(id: int, todo: TodoItem) -> TodoItem:
    load_data()
    if id < 0 or id >= len(todo_list):
        return { "error" : "Todo item not found" }
    todo_list[id] = todo
    save_data()
    return todo

@app.delete("/todo/{id}")
def delete_todo(id: int):
    load_data()
    if id < 0 or id >= len(todo_list):
        return { "error" : "Todo item not found" }
    todo_list.pop(id)
    save_data()
    return

@app.get("/todo/{id}")
def get_todo(id: int) -> TodoItem:
    load_data()
    if id < 0 or id >= len(todo_list):
        return { "error" : "Todo item not found" }
    return todo_list[id]