<!-- Setting up a Flask Server -->
1. Create folder w/ __init__.py file inside
    - inside the file:
    1. from flask import Flask
    2. app = Flask(__name__)
    3. create decorator:
        - @app.route('/')
    4. function
        - def index():
2. Install Flask
    - pip install Flask
3. Install Python-dotenv
    - pipenv install python-dotenv
4. create .flaskenv
    - add FLASK_APP=app
    - add FLASK_DEBUG=True
5. Then to run development server:
    - flask --app 'name of file... in this case __init__' run
    - then server should be running... refer to docs below if not.

- https://flask.palletsprojects.com/en/2.2.x/quickstart/

6. creating secret Key
    - create a config.py file
    - import os
    - create class Config(object):
        - SECRET_KEY = os.environ.get('SECRET_KEY') or 'key-for-devs'
    - add k/v secret key in .flaskenv for actual password


- Summary:
 Basically you just need to install Flask, Python-Dotenv (to set up your environment), create Flask Environemnt (.flaskenv) then run server. 

- Why Flask?
Flask is a lightweight framework that easy to setup and easy to scale projects. I am using it for ease to write API's that I will use to create my Frontend w/ React.  



<!-- setting up WTForms -->
1. install packagees
    - pipenv install Flask-WTF



<!-- Setting up SQLAlchemy -->
1. install packages
    1. 
