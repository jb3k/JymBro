from flask_sqlalchemy import SQLAlchemy
from . import db


class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
    # exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))

    #relationships
    #child of program
    program = db.relationship('Program', back_populates='workout')
    #workouts have many exercises, but exercise can only have 1 workout
    exercise = db.relationship("Exercise", back_populates="workout")


    def to_dict(self):
        return {
            "id": self.id,
            "programId": self.program_id,
            # "exerciseId": self.exercise_id,
        }



# class BodyPart(db.Model):
#     __tablename__ = 'body_part'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     body_part_id = db.Column(db.Integer, db.ForeignKey('Body.id'))

#     #relationships
#     #Each Exercise has a muscle group, 
#     exercise = db.relationship("Exercise", back_populates="workout")
