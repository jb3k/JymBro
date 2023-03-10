<!-- Seeding Data -->

1. Create seed Folder for files
2. from flask.cli import AppGroup
    - what this does is give you seed commands that AppGroup has
    Ex:
    seed_commands = AppGroup('seed')
    - now you can seed your tables w/ following command
    Ex:
    seed_users() for seeding user tables
3. need to create commands to add and undo the seed data
    Ex:
    @seed_commands.command('all') 
    @seed_commands.command('undo')
    -need to add both of these. 'all' to add 'undo' to undo

4. create seed and undo functions below the commands
5. add the seed data like example above

6. Seeding the actual data:
    - import the table and db from models folder
    - create a function that will seed the data 
    Ex: seed_users():
    - One easy way to seed data is to create a list with your data in an object then at the end loop thru the list and get the information from that list
    - db.session.add('info from above')
    - db.session.commit() 
    - print out a messages to let yourself know that it was successful
