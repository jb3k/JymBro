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


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "profileId": self.profile_id,
            "userId": self.user_id
        }
