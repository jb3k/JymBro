from . import db


class User(db.Model):
    __tablename__ = 'users'

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
    #profile to be linked to user
    profile = db.relationship('Profile', back_populates="user", cascade="all, delete")
    #user linked to program
    program = db.relationship('Program', back_populates='user', cascade='all,delete')


#friends table
friends = db.Table(
    'friends',
    db.Model.metadata,
    db.Column('friend_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)




class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    experience_level = db.Column(db.String)
    body_type = db.Column(db.String)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    bio = db.Column(db.String(250))
    goal = db.Column(db.String)
    workout_equipment = goal = db.Column(db.String)
    quantity = db.Column(db.Integer)
    body_part_focus = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('Program.id'))

    #relationships
    #profile to be linked to a user
    user = db.relationship("User", back_populates="profile", cascade='all, delete')
    #profile linked to program
    program = db.relationship("Program", back_populates='profile', cascade='all, delete')
