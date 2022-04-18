from flask import request
from app import app
from ml import Facenet
from app import db

@app.route('/user/register', methods = ["POST"])
def register_user():
    if ('file' not in request.files) or (not request.files['file']):
        return "No image sent", 400
    if ('user' not in request.form) or (not request.form['user']):
        return "No user set", 400
        
    file = request.files['file']
    user = request.form['user']

    try:
        embedding = Facenet.get_embedding(file)   
        db.save_db(embedding, user)
    except Exception as e:
        print(e)

    try:
        db.save_file(file, user)
    except Exception as e:
        print(e)

    return {}

@app.route('/user/login', methods = ["POST"])
def login_user():
    if 'user' not in request.files:
        return "No image sent", 400

    try:
        file = request.files['user']
        embedding = Facenet.get_embedding(file)
        user_id = db.find_user(embedding)
        return user_id
    except Exception as e:
        print(e)
