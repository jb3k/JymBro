from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    users = [
        {
            "first_name": "Demo",
            "last_name": "User",
            "email": "demouser@gmail.com",
            "username": 'demo_user',
            "password": "password"
        }, 
        {
            "email": "user3@gmail.com",
            "first_name": "Rap",
            "last_name": "Monster",
            "password": "password",
            "username": "the_official_rm"
        },
        {
            "email": "user4@gmail.com",
            "first_name": "Ryan",
            "last_name": "Garcia",
            "password": "password",
            "username": "kingryan",
        },
        {
            "email": "user5@gmail.com",
            "first_name": "John",
            "last_name": "Hoffmann",
            "password": "password",
            "username": "johnbob",
            
        },
        {
            "email": "user6@gmail.com",
            "first_name": "Jay",
            "last_name": "Park",
            "password": "password",
            "username": "moresojuplease",
        
        },
        {
            "email": "user7@gmail.com",
            "first_name": "Mohammad",
            "last_name": "Ali",
            "password": "password",
            "username": "jball",
        
        },
        {
            "email": "user8@gmail.com",
            "first_name": "Pikachu",
            "last_name": "de los Rios",
            "password": "password",
            "username": "detective_pikachu",
        
        },
        {
            "email": "user9@gmail.com",
            "first_name": "James",
            "last_name": "Johnson",
            "password": "password",
            "username": "jamesj",
            
        },
        {
            "email": "user10@gmail.com",
            "first_name": "Naruto",
            "last_name": "Uzumaki",
            "password": "password",
            "username": "7thHokage",

        },
        {
            "email": "user11@gmail.com",
            "first_name": "Jennie",
            "last_name": "Kim",
            "password": "password",
            "username": "the_real_jk",
        },
        {
            "email": "user12@gmail.com",
            "first_name": "Lisa",
            "last_name": "Manoban",
            "password": "password",
            "username": "lalalalisa",
            
        }
    ]

    for user in users:

        new_user = User(
            first_name = user["first_name"],
            last_name = user["last_name"],
            username = user["username"],
            email = user["email"],
            password = user["password"],
        )

        db.session.add(new_user)

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
