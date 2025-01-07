from datetime import datetime
#import datetime #not efficient in this case

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%B %d %Y")
print(type(datetime.strptime(deadline, "%B %d %Y")))
print(input_list)

#calculate how many days till the deadline
today_date = datetime.today()
time_till = deadline_date - today_date
print(f"Dear user! Time remaining till your goal: {goal} is {time_till.days} days")
