from pymongo import MongoClient
from flask import Flask, render_template

client = MongoClient(
    "monogodb url"
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
