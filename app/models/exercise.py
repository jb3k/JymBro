from flask_sqlalchemy import SQLAlchemy
from . import db


class Exercise(db.Model):
    __tablename__ = 'exercise'

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

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "muscle": self.muscle,
            "subMuscle": self.sub_muscle,
            "workoutId": self.workout_id,
            "imageUrl": self.image_url,
            "equipment": self.equipment,
            "difficulty": self.difficulty,
            "workoutType": self.workout_type,
            "instructions": self.instructions
        }
