from flask_sqlalchemy import SQLAlchemy
from . import db


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    muscle = db.Column(db.String, nullable= False)
    sub_muscle = db.Column(db.String) 
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    image_url = db.Column(db.String)
    equipment = db.Column(db.String)
    difficulty = db.Column(db.String)
    workout_type = db.Column(db.String)
    instructions = db.Column(db.String)
    # weight = db.Column(db.Integer)
    # sets = db.Column(db.Integer)

    #relationships
    #Child of Workout
    workout = db.relationship('Workout', back_populates='exercise')
