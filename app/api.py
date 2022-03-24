from app import app
from ml import Facenet

@app.route('/')
def hello_world():
    Facenet.get_model()
    return 'tests!'