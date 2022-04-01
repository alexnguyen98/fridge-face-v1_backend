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
        db.save_db(embedding)

        # filename = secure_filename(file.filename)
        # basedir = os.path.abspath(os.path.dirname(__file__))
        # cv2.imwrite(os.path.join(basedir, 'uploads', filename), img)
        # cv2.waitKey(0)

        # filename = secure_filename(file.filename)
        # basedir = os.path.abspath(os.path.dirname(__file__))
        # file.save(os.path.join(basedir, 'uploads', filename))
    except Exception as e:
        print(e)
    return 'tests!'