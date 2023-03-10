<!-- Creating Models -->
1. Imports:
    - from flask_sqlalchemy import SQLAlchemy
    - from . import db
2. create class w/ db.Model as param
3. Enter columns and relationships
4. create to_dict objects for when you want to query the tables



<!-- Connecting to SQLite -->
1. install packages
    - pipenv install alembic
    - pipenv install alembic Flask-Migrate
2. creating database url in .env or .flaskenv
    - EX: DATABASE_URL=sqlite:///dev.db
3. import and setup DB
    - from flask_sqlalchemy import SQLAlchemy
      db = SQLAlchemy()
4. initialize db
    - in main app file (__init__.py inside app folder) import flask, flaskMigrate, and db
    - app.config.from_object(Config)
    - db.init_app(app)
    - Migrate(app,db)







<!-- Backref vs Back_populates -->
- back_populates: needs to go on both parent and child classes    
- backref: only needs to go on one

<!-- One to Many Relationships -->
- You can either have a backref or back_populates
    - if you use backref, you add only to the Parent
    Ex One to Many Relationship w/ backref
        Parent Table: 
        pets = db.relationship('Pet', backref='owner')
        Child Table:
        owner_id = db.relationship('db.Integer, db.ForeignKey('owner.id'))

    - if you use back_populates, you add to the Parent and Child
    Ex: One to Many Relationship w/ back_populates
        Parent:
        workout = db.relationship('Workout', back_populates="program")
        Child: 
        program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
        program = db.relationship('Program', back_populates='workout')


<!-- Many to Many Relationships -->
- create a third table (association table) to connect them.
- just set a variable to third table w/ db.Table('table name', then the columns you want)
    Columns Ex:
    -  db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
- You need to set relationship in the main tables
    - can either use backref or backpopulates
    Ex: Many to Many relationship w/ backref
    following = db.relationship('Channel', secondary=user_channel, backref='followers')
            - Channel is table that you are creating relationship w/
            - secondary being the association table (*NOTE you need to put the association table BEFORE/ABOVE you call on it in the backref)
            - backref is a fake column that you are putting in the table where you have a relationship w/

<!-- Lazy Loading vs Eager Loading -->
