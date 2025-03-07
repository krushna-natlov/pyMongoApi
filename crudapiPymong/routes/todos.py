from fastapi import APIRouter, HTTPException
from models.todos import Todo
from config.database import todo_collection, user_collection
from schema.schemas import list_todo_serial, individual_todo_serial
from bson import ObjectId

router = APIRouter()

@router.get("/todos")
async def get_todos():
    todos = list_todo_serial(todo_collection.find())
    return todos

@router.get("/todos/{todo_id}")
async def get_todo(todo_id: str):
    todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return individual_todo_serial(todo)


@router.post("/todos")
async def create_todo(todo: Todo):
    user = user_collection.find_one({"_id": ObjectId(todo.userId)})
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    new_todo = dict(todo)
    new_todo["userId"] = ObjectId(todo.userId)
    inserted_id = todo_collection.insert_one(new_todo).inserted_id
    return {"_id": str(inserted_id), "message": "Todo created successfully"}


@router.put("/todos/{todo_id}")
async def update_todo(todo_id: str, todo: Todo):
    existing_todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    user = user_collection.find_one({"_id": ObjectId(todo.userId)})
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")

    updated_todo = dict(todo)
    updated_todo["userId"] = ObjectId(todo.userId)

    todo_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": updated_todo})
    return {"message": "Todo updated successfully"}


@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    result = todo_collection.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
@router.get("/todos/user/{user_id}")
async def get_todos_by_user(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    todos = list(todo_collection.find({"userId": ObjectId(user_id)}))
    
    if not todos:
        return {"message": "No todos found for this user"}

    return list_todo_serial(todos)
