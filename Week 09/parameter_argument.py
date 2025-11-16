# --- File: parameter_argument.py ---
# This program demonstrates the difference between
# a parameter and an argument.

print("=" * 50)

# 1. 'your_name' is a PARAMETER.
# A parameter is the variable inside the function's definition.
def greeting(your_name):
    """
    This function takes one parameter and prints a greeting.
    """
    print(f"Welcome {your_name}")

# 2. "Juan" is an ARGUMENT.
# An argument is the actual value that is passed to the function when it is called.
greeting("Juan")