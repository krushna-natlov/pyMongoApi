from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI and MongoDB CRUD API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/")
def create_item(item: dict):
    return {"message": "Item created successfully", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"message": "Item updated successfully", "item_id": item_id, "updated_item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item with ID {item_id} deleted successfully"}
