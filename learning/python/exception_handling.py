# exception handling
# This code demonstrates exception handling in Python.
# It includes a function that raises an exception, and a try-except block to handle it.
# The code also includes a finally block that executes regardless of whether an exception was raised or not.

try:
    # This function raises a ValueError exception
    def raise_exception():
        raise ValueError("An error occurred!")

    # Call the function that raises an exception
    raise_exception()
except ValueError as e:
    # Handle the exception and print the error message
    print(f"Exception caught: {e}")
finally:
    # This block will execute regardless of whether an exception was raised or not
    print("This block always executes.")

# File handling with exception handling
# no raise needed
def open_file(filename):
    try:
        # Try to open the file
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except PermissionError:
        print(f"Error: Permission denied to access file '{filename}'")
    finally:
        # Print a message indicating the operation is complete
        print("File operation complete")

open_file("non-existent-file.txt")

# Custom exception handling
# This code demonstrates how to create and raise a custom exception in Python.
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_input(input_value):
    if input_value < 0:
        raise InvalidInputError("Input value must be non-negative")

try:
    validate_input(-1)
except InvalidInputError as e:
    print(f"Error: {e}")