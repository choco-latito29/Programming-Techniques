# --- File: function_without_arguments.py ---
# This program demonstrates a function that takes no arguments
# and does not return a value (a "procedure").

print("=" * 50)

def calculate_sum_and_print():
    """
    This function receives no arguments.
    It does all the work: gets input, calculates, and prints.
    It does not return any value.
    """
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))

    total = num1 + num2

    print("\n========== REPORT ==========\n")
    print(f"The sum is: {total}")
    print("=" * 50)

def executor():
   """
   Main function to run the program.
   """
   # Calls the function, which runs all the logic
   calculate_sum_and_print()

# --- Start the program ---
executor()