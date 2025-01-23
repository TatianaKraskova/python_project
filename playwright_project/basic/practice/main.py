import requests

username = "TatianaKraskova"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
print(response.text)
print(response.json())
print(type(response.json))
print(response.json()[0])
my_project = response.json()

for project in my_project:
    print(f"Project name: {project['name']} Project URL: {project['url']}")

# from user import User
# from post import Post

# app_user_one = User("nn@nn.com", "Nana", "pwd1", "Devops engineer")
# app_user_one.get_user_info()
#app_user_one.change_job_title("Developer")
#app_user_one.get_user_info()

# app_user_two = User("nn1@nn.com", "Mary", "pwd1", "Teacher")
# app_user_two.get_user_info()
#
# new_post = Post("On a secret mission today", app_user_two.name)
# new_post.get_post_info()

#from helper import validate_and_execute, user_input_message
#from helper import *
# import os
# print(os.name)

# import logging
# logger = logging.getLogger("MAIN")
# logger.error("Error happened in the app")

# user_input = ""
# while user_input != "exit":
#     user_input = input(user_input_message)
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dictionary = {"days":days_and_unit[0], "unit":days_and_unit[1] }
#     print(days_and_unit_dictionary)
#     print(type(days_and_unit_dictionary))
#     validate_and_execute()