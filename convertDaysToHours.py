# Constants
calculation_to_units = 24
name_of_unit = "hours"

# Function to convert days to hours
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered 0. Please enter a valid positive number."
    else:
        return "You entered a negative value. Please enter a valid positive number."

# Function to validate and execute the conversion
def validate_and_execute(num_of_days_element):
    """
    Validates user input and converts days to units if input is a positive integer.
    """
    try:
        # Convert the input to an integer
        user_input_number = int(num_of_days_element)

        # Perform the conversion and print the result
        print(days_to_units(user_input_number))
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Main Program Loop
user_input = ""

while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma-separated list, and I will convert it to hours! ")

    # Exit condition
    if user_input == "exit":
        print("Goodbye!")
        break

    # Split the input into a list
    list_of_days = user_input.split(", ")

    # Debugging prints (optional, can be removed in production)
    print("List of days:", list_of_days)
    print("Set of days:", set(list_of_days))
    print("Type of list_of_days:", type(list_of_days))
    print("Type of set of days:", type(set(list_of_days)))

    # Validate and execute for each element in the list
    for num_of_days_element in set(list_of_days):  # Using `set` to avoid duplicate processing
        validate_and_execute(num_of_days_element)
