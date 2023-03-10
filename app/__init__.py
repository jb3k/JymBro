from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .models import db

app = Flask(__name__)

from app.api import routes

app.config.from_object(Config)
db.init_app(app)
Migrate(app,db)
