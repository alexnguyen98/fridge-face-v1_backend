from flask import request
from app import app
from ml import Facenet
from app import db

# from werkzeug.utils import secure_filename
# import os
# import cv2

@app.route('/')
def hello_world():
    # Facenet.get_model()
    return 'tests!'

@app.route('/user/register', methods = ["POST"])
def register_user():
    if 'user' not in request.files:
        return "No image sent", 400
    try:
        file = request.files['user']
        embedding = Facenet.get_embedding(file)
        id = db.save_db(embedding)
        return id
    except Exception as e:
        print(e)

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