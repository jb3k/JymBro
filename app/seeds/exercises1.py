# from app.models import db, Exercise
# import requests


# def seed_exercise():

#     #retrieve data from API
#     # url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"
#     # querystring = {"muscle":"biceps"}
#     # headers = {
#     #     "X-RapidAPI-Key": "50d59d0504mshcd1e54064668a77p1e96c6jsncaa048b28a6d",
#     #     "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
#     # }
#     # response = requests.request("GET", url, headers=headers, params=querystring)
#     # print(response.text)

#     muscle = 'biceps'
#     api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
#     response = requests.get(api_url, headers={'X-Api-Key': '50d59d0504mshcd1e54064668a77p1e96c6jsncaa048b28a6d'})
#     if response.status_code == requests.codes.ok:
#         exercises = response.text

#         for exercise in exercises:

#             new_exercise = Exercise(
#                 name = exercise["name"],
#                 muscle = exercise["muscle"],
#                 type = exercise["type"],
#                 equipment = exercise["equipment"],
#                 difficulty = exercise["difficulty"],
#                 instructions = exercise["instructions"],
#                 image_url = exercise["image_url"],
#                 sub_muscle = exercise["sub_muscle"],
#                 workout_id = profile["workout_id"],

#             )

#             db.session.add(new_exercise)
        
#         db.session.commit()
#         print('Exercises were succesfully created')

#     else:
#         print("Error:", response.status_code, response.text)



# # Uses a raw SQL query to TRUNCATE the users table.
# # SQLAlchemy doesn't have a built in function to do this
# # TRUNCATE Removes all the data from the table, and RESET IDENTITY
# # resets the auto incrementing primary key, CASCADE deletes any
# # dependent entities
# def undo_exercise():
#     db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
#     db.session.commit()
