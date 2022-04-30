from flask import Flask
import os

app = Flask(__name__)

if (os.environ.get('FLASK_ENV') == 'development'):
    app.config.from_object('config.DevConfig')
else:
    app.config.from_object('config.ProdConfig')

from app import api