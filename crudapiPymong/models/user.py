from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None  # Age is optional

    class Config:
        arbitrary_types_allowed = True  # Allows non-standard types like ObjectId
