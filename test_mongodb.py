from pymongo.mongo_client import MongoClient
uri="mongodb+srv://pratikpadole07_db_user:Pratik1945@cluster0.qujhdq5.mongodb.net/?appName=Cluster0"

client=MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment you Successfully connected to mongoDB!!")
except Exception as e:
    print(e)