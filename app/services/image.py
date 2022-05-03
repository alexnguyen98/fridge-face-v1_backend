from flask import send_from_directory
from app import app
import os
import cv2
import imutils

def get_filename():
        filename = os.path.join(app.root_path, 'static/profile')
        return filename

class ImageService():
    def save_img(self, img, user):
        filename = get_filename()
        img = imutils.resize(img, width=200)
        if not cv2.imwrite(os.path.join(filename, user + ".jpg"), cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)):
            raise Exception("Could not write image")

    def serve_img(self, path):
        filename = get_filename()
        return send_from_directory(filename, path)
