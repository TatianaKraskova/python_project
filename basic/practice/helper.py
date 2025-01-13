# Function to convert days to hours / minutes
from main import days_and_unit_dictionary


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24* 60} minutes"
    else:
        return "unsupported unit"

# Function to validate and execute the conversion
def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0. Please enter a valid positive number.")
        else:
            print("You entered a negative value, no conversion for yo.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

user_input_message = "Hey user, enter number of days and conversion units!\n "