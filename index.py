
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://saurabhkumar244921_db_user:Admin123@cluster0.11dgf59.mongodb.net/?appName=Cluster0"
)

mydb = client["mydatabase"]
mycol = mydb["profiles"]

mycol.insert_one({
    "name": "Kunal Gupta",
    "clg": "Invertis University"
})

print("Profile inserted successfully")