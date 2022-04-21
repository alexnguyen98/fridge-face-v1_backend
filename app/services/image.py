from flask import send_from_directory
from app import app
import os
import cv2
import imutils

def get_filename():
        filename = os.path.join(app.root_path, 'static/profile')
        return filename

class Image():
    def save_img(self, img, user):
        filename = get_filename()
        img = imutils.resize(img, width=200)
        cv2.imwrite(os.path.join(filename, user.lower() + ".jpg"), cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA))

    def serve_img(self, path):
        filename = get_filename()
        return send_from_directory(filename, path)

    def bullshit(self, file):
        filename = get_filename()
        file.peek(0)
        file.save(os.path.join(filename, "bullshit2.jpg"))
