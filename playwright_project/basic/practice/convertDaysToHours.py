# Constants
# calculation_to_units = 24
# name_of_unit = "hours"

# # Function to convert days to hours
# def days_to_units(num_of_days, conversion_unit):
#     if conversion_unit == "hours":
#         return f"{num_of_days} days are {num_of_days * 24} hours"
#     elif conversion_unit == "minutes":
#         return f"{num_of_days} days are {num_of_days * 24* 60} minutes"
#     else:
#         return "unsupported unit"
#
# # Function to validate and execute the conversion
# def validate_and_execute():
#     try:
#         user_input_number = int(days_and_unit_dictionary["days"])
#         if user_input_number > 0:
#             calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
#             print(calculated_value)
#         elif user_input_number == 0:
#             print("You entered 0. Please enter a valid positive number.")
#         else:
#             print("You entered a negative value, no conversion for yo.")
#     except ValueError:
#         print("Invalid input. Please enter a whole number.")
#

# Main Program Loop
# user_input = ""
# while user_input != "exit":
#     user_input = input("Hey user, enter number of days as a comma-separated list, and I will convert it to hours! ")
#
#     # Exit condition
#     if user_input == "exit":
#         print("Goodbye!")
#         break
#
#     # Split the input into a list
#     list_of_days = user_input.split(", ")
#
#     # Debugging prints (optional, can be removed in production)
#     print("List of days:", list_of_days)
#     print("Set of days:", set(list_of_days))
#     print("Type of list_of_days:", type(list_of_days))
#     print("Type of set of days:", type(set(list_of_days)))
#
#     # Validate and execute for each element in the list
#     for num_of_days_element in set(list_of_days):  # Using `set` to avoid duplicate processing
#         validate_and_execute(num_of_days_element)

# print("some text")
# input("enter value")
# set([1,2,4])
# int("20")

# via dictionary key:value pairs; is a collectio, which doesn`t allow duplicate values
# user_input = ""
# while user_input != "exit":
#     user_input = input("Hey user, enter number of days and conversion units!\n ")
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dictionary = {"days":days_and_unit[0], "unit":days_and_unit[1] }
#     print(days_and_unit_dictionary)
#     print(type(days_and_unit_dictionary))
#     validate_and_execute()


"""my_list = ["20", "30", "100"] #how to access list / dictionary
print(my_list[2])
my_dictionary = {"days":20, "unit": "hours"}
print(my_dictionary["days"])
print(my_dictionary["unit"])"""
