from flask_sqlalchemy import SQLAlchemy
from . import db

class Program(db.Model):
    __tablename__ = 'program'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))

    #relationships
    #Child of User
    user = db.relationship("User", back_populates="program", cascade='all, delete')
    #Child of Profile
    profile = db.relationship('Profile', back_populates="program", cascade="all, delete")
    #Parent of workout
    workout = db.relationship('Workout', back_populates="program")



class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
    # exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))

    #relationships
    #child of program
    program = db.relationship('Program', back_populates='workout')
    #workouts have many exercises, but exercise can only have 1 workout
    exercise = db.relationship("Exercise", back_populates="workout")



class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    body_part = db.Column(db.String, nullable= False)
    sub_body_part = db.Column(db.String, nullable= False) 
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    image_url = image_url = db.Column(db.String)
    # weight = db.Column(db.Integer)
    # sets = db.Column(db.Integer)

    #relationships
    #Child of Workout
    workout = db.relationship('Workout', back_populates='exercise')




# class BodyPart(db.Model):
#     __tablename__ = 'body_part'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     body_part_id = db.Column(db.Integer, db.ForeignKey('Body.id'))

#     #relationships
#     #Each Exercise has a muscle group, 
#     exercise = db.relationship("Exercise", back_populates="workout")
