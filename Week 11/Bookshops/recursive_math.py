# --- File: Bookshops/recursive_math.py ---
# This file is a MODULE.
# It defines several math functions using recursion.

def factorial(n):
    """Calculates factorial recursively (e.g., n!)."""
    # Base Case: The stopping condition
    if n == 0:
        return 1
    # Recursive Step: The function calls itself
    else:
        return n * factorial(n - 1)


def multiplica(num1, num2):
    """Calculates multiplication using recursive addition."""
    # Base Case 1: Anything * 0 is 0
    if (num1 == 0 or num2 == 0):
        return 0
    # Base Case 2: Anything * 1 is itself
    elif (num2 == 1):
        return num1
    # Recursive Step: 5 * 3 is 5 + (5 * 2)
    else:
        return num1 + multiplica(num1, num2 - 1)


def potencia(base, exponente):
    """Calculates exponentiation using recursive multiplication."""
    # Base Case: Anything ^ 0 is 1
    if (exponente == 0):
        return 1
    # Recursive Step: 2 ^ 3 is 2 * (2 ^ 2)
    else:
        return base * potencia(base, exponente - 1)