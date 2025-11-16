# --- File: Bookshops/arithmetic_operations.py ---
# This file is a MODULE.
# It defines basic arithmetic functions for reuse in other programs.

def add(num1, num2):
    """Adds two numbers and returns the sum."""
    sum_val = num1 + num2
    return sum_val

def subtract(num1, num2):
    """Subtracts the second number from the first and returns the difference."""
    rest = num1 - num2
    return rest

def multiply(num1, num2):
    """Multiplies two numbers and returns the product."""
    mult = num1 * num2
    return mult

def divide(num1, num2):
    """Divides the first number by the second and returns the quotient."""
    # Note: This function will crash if num2 is 0.
    div = num1 / num2
    return div