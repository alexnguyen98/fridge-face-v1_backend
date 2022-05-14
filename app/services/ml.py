from mtcnn.mtcnn import MTCNN
from tensorflow import keras
import numpy
import cv2

mtcnn = MTCNN()

def read_image(img):
        img = cv2.imdecode(numpy.fromstring(img.read(), numpy.uint8), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

def crop_bb(img, detection, margin):
    x1, y1, w, h = detection['box']
    x1 -= margin
    y1 -= margin
    w += 2*margin
    h += 2*margin
    if x1 < 0:
        w += x1
        x1 = 0
    if y1 < 0:
        h += y1
        y1 = 0
    return img[y1:y1+h, x1:x1+w]

def crop(img):
    try:
        det = mtcnn.detect_faces(img)[0]
        margin = int(0.1 * img.shape[0])
        img = crop_bb(img, det, margin);
        return img
    except Exception as e:
        raise Exception("No face found")

def process_face(img):
    img = cv2.resize(img, (160, 160))
    img = img.astype('float32')
    # because facenet is pretrained with normalised inputs
    mean, std = img.mean(), img.std();
    img = (img - mean) / std
    return img

class MlService:
    model = None

    def __init__(self):
        try:
            print("* Loading model...")
            self.model = keras.models.load_model('./model/facenet_keras.h5')
            print("* Model loaded")
        except Exception as e:
            print(e)

    def process_img(self, img):
        img = read_image(img)
        img = crop(img)
        return img

    def get_embedding(self, img):
        face = process_face(img)
        face = numpy.expand_dims(face, axis=0)
        return self.model.predict(face)
