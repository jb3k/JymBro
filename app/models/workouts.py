from flask_sqlalchemy import SQLAlchemy
from . import db

class Program(db.Model):
    __tablename__ = 'program'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('Profile.id'))

    #relationships
    #profile to be linked to a user
    user = db.relationship("User", back_populates="program", cascade='all, delete')
    #profile linked to program
    profile = db.relationship('Profile', back_populates="program", cascade="all, delete")
