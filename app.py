# app.py
from flask import Flask, render_template
from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def todo_form():
    return render_template('todo.html')
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
