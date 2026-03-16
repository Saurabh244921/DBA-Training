
from pymongo import MongoClient

client = MongoClient(
    "monogodb Url"
)

mydb = client["mydatabase"]
mycol = mydb["profiles"]

mycol.insert_one({
    "name": "Kunal Gupta",
    "clg": "Invertis University"
})

print("Profile inserted successfully")
