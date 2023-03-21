from app.models import db, User
import random

users_dictionary = {}


# Adds a demo user, you can add other users here if you want
def seed_users():

    global users_dictionary

    users = [
        {
            "first_name": "Demo",
            "last_name": "User",
            "email": "demouser@gmail.com",
            "username": 'demo_user',
            "password": "password"
        }, 
        {
            "email": "user1@gmail.com",
            "first_name": "Mohammad",
            "last_name": "Ali",
            "password": "password",
            "username": "jball"
        },
        {
            "email": "user2@gmail.com",
            "first_name": "Naruto",
            "last_name": "Uzumaki",
            "password": "password",
            "username": "7thHokage"
        }
    ]


    # looping thru the list of users i created above and adding them to the db
    for user in users:

        new_user = User(
            first_name = user["first_name"],
            last_name = user["last_name"],
            username = user["username"],
            email = user["email"],
            password = user["password"],
        )

        db.session.add(new_user)


    # 
    # for i, user in enumerate(users):
    #     users_dictionary[f'user{i+1}'] = User(
    #         email = user["email"],
    #         first_name = user["first_name"],
    #         last_name = user["last_name"],
    #         password = user["password"],
    #         username = user["username"]
    #     )

    # for user in users_dictionary.values():
    #     max_range = random.randint(0, 3)
    #     new_set = set()
    #     for i in range(max_range):
    #         random_user=random.choice(list(users_dictionary.values()))
    #         # if random_user is not current user, then add to set.  If it is current user, do nothing.
    #         if random_user.username != user.username:
    #             new_set.add(random_user)

    #     # for each user add following_id = list(new_set)
    #     user.followers = list(new_set)
    

    db.session.commit()
    print('Users were succesfully created')


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
