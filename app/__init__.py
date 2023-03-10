from flask import Flask
from .config import Config
from .models import db

app = Flask(__name__)

from app.api import routes

app.config.from_object(Config)
db.init_app(app)
