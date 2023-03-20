from flask.cli import AppGroup

# import the seed data from each file
from .users import seed_users, undo_users
from .profile import seed_profile, undo_profile
from .workouts import seed_workout, undo_workout
from .programs import seed_program, undo_program
from .exercises import seed_exercise, undo_exercise



# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    # Add other seed functions here
    seed_profile()
    seed_program()
    seed_workout()
    seed_exercise()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
    undo_profile()
    undo_program()
    undo_workout()
    undo_exercise()

#force upload
