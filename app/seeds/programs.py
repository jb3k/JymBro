from app.models import db, Program


# Adds a demo user, you can add other users here if you want
def seed_program():

    programs = [
        {
            "name": "Bulk",
            "workout_id": 1,
            "user_id":1
        },
        {
            "name": "Cut",
            "workout_id": 2,
            "user_id": 2
        },
        {
            "name": "Performance",
            "workout_id": 3,
            "user_id": 3
        }

    ]

    for program in programs:

        new_program = Program(
            name = program["name"],
            workout_id = program["workout_id"],
            user_id = program["user_id"],
        )

        db.session.add(new_program)

    db.session.commit()
    print('Programs were succesfully created')


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_program():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
