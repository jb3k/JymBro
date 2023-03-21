from flask_sqlalchemy import SQLAlchemy
from . import db

#friends table
friends = db.Table(
    'friends',
    db.Model.metadata,
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    user_name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    password = db.Column(db.String(30))


    #relationships:
    #friend has a relationship with users... 
    friend = db.relationship(
        "User",
        secondary=friends,
        primaryjoin=(friends.c.friend_id == id),
        secondaryjoin=(friends.c.user_id == id),
        backref=db.backref('following', lazy='joined'),
        lazy='joined'
    )
    #Parent of Profile
    profile = db.relationship('Profile', back_populates="user", cascade="all, delete")
    # Parent of Program
    program = db.relationship('Program', back_populates='user', cascade='all,delete')


    def to_dict(self):
        return {
            'id': self.id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'password': self.password,
            'userName': self.user_name
        }
