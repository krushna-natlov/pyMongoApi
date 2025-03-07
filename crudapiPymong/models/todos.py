from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Todo(BaseModel):
    name: str
    description: str
    completed: bool
    userId: str  

    class Config:
        arbitrary_types_allowed = True 
