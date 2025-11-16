# --- File: factorial_main.py ---
# This program defines a recursive factorial function
# and then executes it based on user input.

def factorial(n):
    """
    Calculates the factorial of 'n' using recursion.
    """

    # 1. The Base Case (Stopping condition)
    # The factorial of 0 (0!) is 1.
    if (n == 0):
        return 1

    # 2. The Recursive Step
    # n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


def executor():
    """
    Main function to get user input and print the result.
    """

    # --- Validation Loop ---
    while True:
        num = int(input("Enter a number for factorial: "))

        if (num < 0):
            print("[ERROR] Please re-enter a non-negative number...")
        else:
            break  # Exit the loop if the number is valid

    # Call the recursive function
    result = factorial(num)

    print(f"The factorial is: {result}")


# --- Start the program ---
executor()