from flask import Flask
from app.config import Config

app = Flask(__name__)

from app.api import routes

app.config.from_object(Config)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
