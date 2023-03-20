<!-- Session  -->
1. import at top from flask




<!-- alembic -->
1. install in home directory with app  and react-app 
    - pipenv run alembic init alembic
    - The env.py file is really important. When you run all of the other Alembic commands, Alembic will load the env.py file to configure the environment. A following section will highlight some important things for you to consider.
    - The script.py.mako file is the template that Alembic uses to generate the migration scripts that you tell it to generate. You can customize it so that it fits your needs. That's polite of Alembic. Thanks, Alembic!
2. 

What is alembic?
- Alembic is a lightweight database migration tool that allows developers to easily manage changes to their database schema over time. It provides a way to automate the process of creating, modifying, and deleting database tables, columns, and indexes, and keeping the database schema in sync with the codebase.

Why alembic?
- using Alembic with Python provides a reliable and efficient way to manage database schema changes, while also allowing developers to leverage the flexibility and power of Python.

<!-- Using alembic with Flask -->
1. install flask-migrate
    - pipenv install alembic Flask-Migrate
2. make sure you have the DB URL in .env or .flaskenv
3. import SQLAlchemy in models folder and also import all of the models from your files
    Code:
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy()
4. make sure you models and seed data are connected to the init__app file
    code: (need these lines in init__app to let flask about seed commands)
    ```
    from .seeds import seed_commands
    app.cli.add_command(seed_commands)
    ```

5. initialize flask 
    - pipenv run flask db init
    - this will create the migrations folder with the files from above.
6. migrate and upgrade
    - pipenv run flask db migrate
    - pipenv run flask db upgrade

    - migrate to generate migration
    - upgrade to apply to db
