# --- File: Electricity/data_input.py ---
# This module handles user input validation.

def read_positive_float(message):
    """Reads a float. Loops if the value is 0 or negative."""
    while True:
        # Direct conversion as per your original code
        value = float(input(message))

        if (value <= 0):
            print("[ERROR] The value must be positive.")
        else:
            return value

def read_menu_option(message, min_op, max_op):
    """Reads an integer menu option within a range."""
    while True:
        op = int(input(message))

        if (op < min_op or op > max_op):
            print(f"[ERROR] Invalid option. Enter between {min_op} and {max_op}.")
        else:
            return op

def read_category(message):
    """Reads a category (A-E)."""
    while True:
        cat = input(message).upper()

        # Logic: If it IS in the list, return it. Else, print error.
        if cat in ['A', 'B', 'C', 'D', 'E']:
            return cat
        else:
            print("[ERROR] Invalid category. Enter a category between A and E.")