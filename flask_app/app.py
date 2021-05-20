from flask import Flask
from database import db, ma

app = Flask(__name__)

from flask_app import config

db.init_app(app)
ma.init_app(app)
