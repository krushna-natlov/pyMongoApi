from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]

todo_collection = db["todos"]
user_collection = db["users"]  
