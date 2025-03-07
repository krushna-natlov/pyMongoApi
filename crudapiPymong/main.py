from fastapi import FastAPI
from routes.todos import router as todo_router
from routes.user import router as user_router

app = FastAPI()

app.include_router(todo_router, prefix="/api")
app.include_router(user_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Todo API"}
