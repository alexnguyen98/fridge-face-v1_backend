from mtcnn.mtcnn import MTCNN
from keras.models import load_model
import numpy
import cv2

mtcnn = MTCNN()

def get_model():
    global model # singleton model
    if (not 'model' in globals()):
        try:
            print("* Loading model...")
            model = load_model('./ml/facenet_keras.h5')
            print("* Model loaded")
        except Exception as e:
            print(e)
    return model

def read_image(file):
    img = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
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

def crop(file):
    det = mtcnn.detect_faces(file)[0]
    margin = int(0.1 * file.shape[0])
    img = crop_bb(file, det, margin);
    return img

def process_face(file):
    img = cv2.resize(file, (160, 160))
    img = img.astype('float32')
    # because facenet is pretrained with normalised inputs
    mean, std = img.mean(), img.std();
    img = (img - mean) / std
    return img

def get_embedding(file):
    model = get_model()
    img = read_image(file)
    img = crop(img)
    face = process_face(img)
    face = numpy.expand_dims(face, axis=0)
    return model.predict(face)