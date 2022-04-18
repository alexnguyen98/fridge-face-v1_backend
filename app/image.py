from flask import send_from_directory
import os

def get_filename():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(base_dir, 'static/profile')
    return filename

def save_file(file, user):
    filename = get_filename()
    file.seek(0)
    file.save(os.path.join(filename, user + ".jpg"))

def serve_img(path):
    filename = get_filename()
    return send_from_directory(filename, path)
