from app.models import db, Workout


# Adds a demo user, you can add other users here if you want
def seed_workout():

    workouts = [
        {"program_id": 1},
        {"program_id": 2},
        {"program_id": 3},

    ]

    for workout in workouts:

        new_workout = Workout(
            program_id = workout['program_id']
        )

        db.session.add(new_workout)

    db.session.commit()
    print('Workouts were succesfully created')


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_workout():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
