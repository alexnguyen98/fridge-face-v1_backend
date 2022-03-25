from flask import request
from crypt import methods
from app import app
from ml import Facenet

@app.route('/')
def hello_world():
    # Facenet.get_model()
    return 'tests!'

@app.route('/user/register', methods = ["POST"])
def register_user():
    print(request.files)
    print(request.form)
    if 'user' not in request.files:
        return "No image sent", 400
    print(request.files["user"])
    return 'tests!'