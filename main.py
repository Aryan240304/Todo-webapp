from fastapi import FastAPI
from pydantic import Baseodel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Todo(BaseModel):
    id: int
    name: str
    description: str

# Start with an empty list
todos: list[Todo] = []

@app.get("/get_todo")
def show_todos():
    return todos

@app.post("/append_todo")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully"}


@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    global todos
    todos = [todo for todo in todos if todo.id != id]
    return {"message": "Todo deleted successfully"}

@app.put("/update_todo/{id}")
def update_todo(id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully"}
    return {"message": "Todo not found"}