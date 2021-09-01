import os, json, requests

from flask import Flask
from flask import request
from io import BytesIO
from tensorflow import keras
from PIL import Image

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'tests!'

@app.route('/face', methods=['POST'])
def recognize_face():
    if 'img' not in request.files:
        return "No image sent", 400

    img = Image.open(BytesIO(request.files["img"].read()))
    img.resize((150, 150))
    img = keras.preprocessing.image.img_to_array(img) / 255.
    img = img.astype('float16')
    payload = json.dumps({'instances': img.tolist()})
    res = requests.post('http://tfserving:8501/v1/models/facenet:predict', json=payload)
    print(json.loads(res.text))
    
    return 'works!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

# 10.0.1.37