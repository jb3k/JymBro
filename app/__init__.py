from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .models import db
from .seeds import seed_commands

app = Flask(__name__)

from app.api import routes

# Tell flask about our seed commands
app.cli.add_command(seed_commands)



app.config.from_object(Config)
db.init_app(app)
Migrate(app,db)
