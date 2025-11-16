# --- File: recursive_equation.py ---
# This is a MAIN program that imports and uses the 'recursive_math' module
# to solve the equation: z = (n! - (a*b)) / n

# 1. Import the 'recursive_math' module and give it an alias 'recursv'
# (This assumes the file 'recursivas.py' was renamed to 'recursive_math.py')
import Bookshops.recursive_math as recursv

print("=" * 50)


def calculate():
    """Main logic function"""

    # --- Validation loop for n (must be >= 0) ---
    while True:
        n = int(input("Enter the value of n: "))
        if (n < 0):
            print("[ERROR] re-enter")
        else:
            break

    # --- Validation loop for a (must be >= 0) ---
    while True:
        a = float(input("Enter the value of a: "))
        if (a < 0):
            print("[ERROR] re-enter")
        else:
            break

    # --- Validation loop for b (must be >= 0) ---
    while True:
        b = float(input("Enter the value of b: "))
        if (b < 0):
            print("[ERROR] re-enter")
        else:
            break

    # --- Calculations using the imported module ---
    # Call the factorial function from the 'recursv' module
    fact = recursv.factorial(n)
    # Call the multiplica function from the 'recursv' module
    mult = recursv.multiplica(a, b)

    subtraction = fact - mult

    # --- Division and Output ---
    # Check for ZeroDivisionError before calculating 'z'
    if (n != 0):
        z = subtraction / n
        print(f"The result value of the equation Z is: {z}")
    else:
        print("[ERROR] Cannot divide by zero")

    # --- Final Report ---
    print(f"The factorial value of {n} is: {fact}")

    # --- Logical Anomaly ---
    # The print message says "multiplication", but it prints the 'subtraction' variable.
    print(f"The multiplication value of {a} and {b} is: {subtraction}")


# --- Start the program ---
calculate()