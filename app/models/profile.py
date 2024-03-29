from flask_sqlalchemy import SQLAlchemy
from . import db

class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    experience_level = db.Column(db.String)
    body_type = db.Column(db.String)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    bio = db.Column(db.String(250))
    goal = db.Column(db.String)
    workout_equipment = db.Column(db.String)
    quantity = db.Column(db.Integer)
    body_part_focus = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # program_id = db.Column(db.Integer, db.ForeignKey('program.id'))

    #relationships
    #Child of User
    user = db.relationship("User", back_populates="profile", cascade='all, delete')
    #Paremt of Program
    program = db.relationship("Program", back_populates='profile', cascade='all, delete')


    def to_dict(self):
        return {
            "id": self.id,
            "experienceLevel": self.experience_level,
            "bodyType": self.body_type,
            "height": self.height,
            "weight": self.weight,
            "bio": self.bio,
            "goal": self.goal,
            "workoutEquipment": self.workout_equipment,
            "quantity": self.quantity,
            "bodyFocus": self.body_part_focus,
            "userId": self.user_id
        }
