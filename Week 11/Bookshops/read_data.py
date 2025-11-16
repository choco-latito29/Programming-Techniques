# --- File: Bookshops/read_data.py ---
# This file is a MODULE.
# It is not meant to be run directly.
# Its purpose is to store reusable helper functions
# for reading and validating user input.

def read_positive_float(message):
    """Loops until the user enters a float greater than 0."""
    while True:
        value = float(input(message))

        if (value <= 0):
            print("[ERROR] Please re-enter, value must be positive.")
        else:
            return value


def read_positive_int(message):
    """Loops until the user enters an integer greater than 0."""
    while True:
        value = int(input(message))

        if (value <= 0):
            print("[ERROR] Please re-enter, value must be positive.")
        else:
            return value


def read_gender(message):
    """Loops until the user enters 'F' or 'M'."""
    while True:
        gender_upper = input(message).upper()

        if (gender_upper != 'F' and gender_upper != 'M'):
            print("[ERROR] Please re-enter (M/F).")
        else:
            return gender_upper


def read_menu_option(message, min_op, max_op):
    """Loops until the user enters an integer within a valid range."""
    while True:
        op = int(input(message))
        if (op < min_op or op > max_op):
            print(f"[ERROR] Please re-enter (Option from {min_op} to {max_op}).")
        else:
            return op