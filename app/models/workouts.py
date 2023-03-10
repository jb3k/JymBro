from flask_sqlalchemy import SQLAlchemy
from . import db

class Program(db.Model):
    __tablename__ = 'program'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('Workout.id'))

    #relationships
    #profile to be linked to a user
    user = db.relationship("User", back_populates="program", cascade='all, delete')
    #profile linked to program
    profile = db.relationship('Profile', back_populates="program", cascade="all, delete")



class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    # sets = db.Column(db.Integer)
    # reps = db.Column(db.Integer)
    exercise_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    #relationships
    #workouts have many exercises, but exercise can only have 1 workout
    exercise = db.relationship("Exercise", back_populates="workout")



class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body_part_id = db.Column(db.Integer, db.ForeignKey('Body.id'))

    #relationships
    #Each Exercise has a muscle group, 
    exercise = db.relationship("Exercise", back_populates="workout")



class BodyPart(db.Model):
    __tablename__ = 'body_part'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body_part_id = db.Column(db.Integer, db.ForeignKey('Body.id'))

    #relationships
    #Each Exercise has a muscle group, 
    exercise = db.relationship("Exercise", back_populates="workout")



class SubBodyPart(db.Model):
    __tablename__ = 'sub_body_part'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    body_part_id = db.Column(db.Integer, db.ForeignKey('Body.id'))

    #relationships
    #Each Exercise has a muscle group, 
    exercise = db.relationship("Exercise", back_populates="workout")
