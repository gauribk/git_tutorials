from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# Replace with your actual MongoDB connection string
MONGO_URI = "your_mongodb_connection_string"
client = MongoClient(MONGO_URI)
db = client['myDatabase']
collection = db['users']  # Or any collection name

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        # Input validation (basic)
        if not name or not age:
            return render_template('form.html', error="Name and age are required.")

        try:
            collection.insert_one({'name': name, 'age': int(age)})
            return redirect(url_for('success'))
        except Exception as e:
            return render_template('form.html', error=f"Error: {e}")

    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
