from pymongo import MongoClient

if __name__ == '__main__':
    print("Welcome to pymongo")
    client = MongoClient('mongodb://localhost:27017')
    print(client)
    # allDatabase = client.list_database_names()
    # print(allDatabase)

    # collection = client['testDb']
    # print(collection.list_collection_names())

    #insert one document 

    database = client['testDb']
    collection1 = database['testCollection']

    dictionary = {
        "name": "John",
        "age": 25,
        "city": "New York"
    }

    # collection1.insert_one(dictionary)
    
    insert_list = [
        {"name": "Alice", "age": 30, "city": "London"},
        {"name": "Bob", "age": 28, "city": "Paris"},
        {"name": "Charlie", "age": 32, "city": "Berlin"},
        {"name": "David", "age": 35, "city": "Tokyo"}

    ]

    collection1.insert_many(insert_list)

    read = collection1.find_one({"name": "Bob"})
    print(read)

    # update document
    
    # collection1.update_one({"name": "Bob"}, {"$set": {"city": "Mumbai"}})