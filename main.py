calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    #condition_check = num_of_days > 0
    #print(type(condition_check)) // to check the type

    if num_of_days > 0:
        return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    elif num_of_days == 0:
        return "You entered a 0, please enter a valid positive num"
    else:
        return "You entered a negative value, please enter a valid positive num"

days_to_units(5)
# days_to_units(10)
# days_to_units(10)


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(num_of_days_element)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("Your input is not a number")


# while True:
#     user_input = input("Hey user, enter a number of days\n")
#     validate_and_execute()

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days\n")
    for num_of_days_element in user_input.split(","):
        validate_and_execute()

# list [2, 4, 6]