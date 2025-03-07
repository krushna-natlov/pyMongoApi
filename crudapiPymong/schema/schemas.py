def individual_todo_serial(todo) -> dict:
    return {
        "_id": str(todo["_id"]), 
        "description": todo["description"],
        "completed": todo["completed"],
        "userId": str(todo["userId"])  
    }

def list_todo_serial(todos) -> list:
    return [individual_todo_serial(todo) for todo in todos]


def individual_user_serial(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }

def list_user_serial(users) -> list:
    return [individual_user_serial(user) for user in users]