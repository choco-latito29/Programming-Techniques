# --- File: recursion.py ---
# This program defines a recursive function to calculate the factorial of a number.

def factorial(n):
    """
    Calculates the factorial of 'n' using recursion.
    """

    # 1. The Base Case:
    # This is the condition that stops the recursion.
    # The factorial of 0 (0!) is defined as 1.
    if (n == 0):
        return 1

    # 2. The Recursive Step:
    # The function calls itself with a smaller version of the problem.
    # The factorial of n (n!) is n * (n-1)!
    else:
        return n * factorial(n - 1)

# Note: This file only defines the function.
# To use it, you would need to call it, for example:
# print(factorial(5))