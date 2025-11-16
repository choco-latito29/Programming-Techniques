# --- File: function_with_args.py ---
# This program demonstrates passing arguments to a function
# that performs an action (prints) but does not return a value.

print("=" * 50)

def calculate_sum(n1, n2):
    """
    This function RECEIVES n1 and n2 as parameters.
    It calculates their sum and prints the report itself.
    It does not return any value.
    """
    total = n1 + n2

    print("\n========== REPORT ==========\n")
    print(f"The sum is: {total}")
    print("=" * 50)

def executor():

    # The executor function is responsible for getting the data
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))

    # --- Argument Passing ---
    # The values of num1 and num2 are passed as ARGUMENTS
    # to the calculate_sum function, which receives them
    # as PARAMETERS n1 and n2.
    calculate_sum(num1, num2)

# --- Start the program ---
executor()