import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

import_dotenv = load_dotenv()

FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:8000')

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client.userlist
collection = db['flask-users']

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_button():
    try:
        
        name = request.form.get('name')
        role = request.form.get('role')
        user_id = request.form.get('id')

        collection.insert_one({
            "id": user_id,
            "name": name,
            "role": role
        })
        
        print(f"Successfully inserted: {name}")

        return redirect(f"{FRONTEND_URL}/success")
    
    except Exception as e:
        print(f"Error: {e}")
        return redirect('http://localhost:5000/')

@app.route('/success')
def success():
    return "<h1>Data submitted successfully!</h1>"

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)