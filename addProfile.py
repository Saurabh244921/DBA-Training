from pymongo import MongoClient
from flask import Flask, render_template

client = MongoClient(
    "mongodb+srv://saurabhkumar244921_db_user:Admin123@cluster0.11dgf59.mongodb.net/?appName=Cluster0"
)

mydb = client["mydatabase"]
mycol = mydb["profiles"]

app = Flask(__name__)

@app.route('/')
def home():
    data = mycol.find_one()
    if data is None:
        return "No data found in database"
    return render_template('index.html', name=data["name"])

if __name__ == '__main__':
    app.run(debug=True)