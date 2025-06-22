# app.py
from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.todo_db
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    item_name = request.form['itemName']
    item_description = request.form['itemDescription']
    collection.insert_one({
        'name': item_name,
        'description': item_description
    })
    return redirect('/')
