from flask import request, jsonify
from app import app
from app.db import DB
from app.services.ml import ML
from app.services.image import Image

db = DB()
ml = ML()
image = Image()

@app.route('/user/list')
def get_usernames():
    try:
        return jsonify(users=db.get_avaiable_users())
    except Exception as e:
        print(e)
    
    return {}

@app.route('/uploads/<path:path>')
def serve_image(path):
    try:
        return image.serve_img(path)
    except Exception as e:
        print(e)
    
    return {}

# NOTICE: For testing!
@app.route('/reset')
def reset():
    db.reset_db()
    return {}

@app.route('/image/test2', methods = ["POST"])
def imageTest2():
    if ('file' not in request.files) or (not request.files['file']):
        return "No image sent", 400
    
    file = request.files['file']

    try:
        image.bullshit(file)
    except Exception as e:
        print(e)

    return {}

@app.route('/user/register', methods = ["POST"])
def register_user():
    if ('file' not in request.files) or (not request.files['file']):
        return "No image sent", 400
    if ('user' not in request.form) or (not request.form['user']):
        return "No user set", 400

    file = request.files['file']
    user = request.form['user']
    img = None

    if (not db.user_exist(user)):
        return "User doesnt exist", 403
    if (db.registered_exist(user)):
        return "User already registered", 403

    try:
        img = ml.process_img(file)
        embedding = ml.get_embedding(img)
        db.save_db(embedding, user)
        image.save_img(img, user)
        return jsonify(token="temporary_access_token=" + user)
    except Exception as e:
        print(e)

    return {}

@app.route('/user/login', methods = ["POST"])
def login_user():
    if 'user' not in request.files:
        return "No image sent", 400

    try:
        file = request.files['user']
        img = ml.process_img(file)
        embedding = ml.get_embedding(img)
        user = db.find_user(embedding)
        if (user):
            return jsonify(token="temporary_access_token=" + user)
    except Exception as e:
        print(e)

    return {}
