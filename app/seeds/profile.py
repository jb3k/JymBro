from app.models import db, Profile


def seed_profile():

    profiles = [
        {
           " experience_level": 'Beginner',
            "body_type": 'slim',
            "height": 156,
            "weight": 100,
            "bio": 'I am a skinny person looking to start working out',
            "goal": 'bulk up',
            "workout_equipment": 'home',
            "quantity": 4,
            "body_part_focus": 'chest',
            "user_id": 1
        },
        {
           " experience_level": 'Intermediate',
            "body_type": 'lean',
            "height": 200,
            "weight": 160,
            "bio": 'I am a trying to perform better',
            "goal": 'performance',
            "workout_equipment": 'commercial gym',
            "quantity": 5,
            "body_part_focus": 'chest',
            "user_id": 2
        },
        {
           " experience_level": 'Beginner',
            "body_type": 'fat',
            "height": 180,
            "weight": 400,
            "bio": 'I am obese, i want to lose weight',
            "goal": 'lose weight',
            "workout_equipment": 'home gym',
            "quantity": 4,
            "body_part_focus": 'None',
            "user_id": 3
        },
    ]

    for profile in profiles:

        new_profile = Profile(
            experience_level = profile["experience_level"],
            body_type = profile["body_type"],
            height = profile["height"],
            weight = profile["weight"],
            bio = profile["bio"],
            goal = profile["goal"],
            workout_equipment = profile["workout_equipment"],
            quantity = profile["quantity"],
            body_part_focus = profile["body_part_focus"],
            user_id = profile["user_id"],
        )

        db.session.add(new_profile)

    db.session.commit()
    print('Profiles were succesfully created')


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_profile():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
