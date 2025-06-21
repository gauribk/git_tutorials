from flask import request
from pymongo import MongoClient

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")

    if not item_name or not item_desc:
        return "Missing fields", 400

    collection.insert_one({"name": item_name, "description": item_desc})
    return "Item submitted successfully!", 200
