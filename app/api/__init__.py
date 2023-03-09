from app import app
from .routes import login

@app.route('/')
def home():
    return '<h1> TESTER </h1>'
