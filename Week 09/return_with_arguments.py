# --- File: return_with_arguments.py ---
# This program demonstrates a function that
# RECEIVES arguments and RETURNS a value.

print("=" * 50)

def calculate_sum(n1, n2):
    """
    Receives 'n1' and 'n2' as parameters,
    calculates the sum, and returns the result.
    """
    total = n1 + n2
    # 'return' sends the calculated value back
    return total

def executor():
    """
    Main function to get data and print the report.
    """

    # 1. Get data from the user
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))

    # 2. Pass the data as arguments to the function.
    # The returned value is captured in the 's' variable.
    s = calculate_sum(num1, num2)

    # 3. Print the result
    print("\n========== REPORT ==========\n")
    print(f"The sum is: {s}")
    print("=" * 50)

# --- Start the program ---
executor()