# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def todo_form():
    return render_template('todo.html')
