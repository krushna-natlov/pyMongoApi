from fastapi import APIRouter, HTTPException
from models.user import User
from config.database import user_collection
from schema.schemas import list_user_serial, individual_user_serial
from bson import ObjectId

router = APIRouter()


@router.get("/users")
async def get_users():
    users = list_user_serial(user_collection.find())
    return users

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return individual_user_serial(user)

@router.post("/users")
async def create_user(user: User):
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = dict(user)
    inserted_id = user_collection.insert_one(new_user).inserted_id
    return {"_id": str(inserted_id), "message": "User created successfully"}


@router.put("/users/{user_id}")
async def update_user(user_id: str, user: User):
    existing_user = user_collection.find_one({"_id": ObjectId(user_id)})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = dict(user)
    user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user})
    return {"message": "User updated successfully"}


@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
