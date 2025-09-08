from fastapi import FastAPI
from pydantic import BaseModel
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
