# --- File: calculate.py ---
# This is a MAIN program.
# It demonstrates two ways to import and use the 'arithmetic_operations' module.

# 1. Import the entire module and give it a nickname ('calculator')
import Bookshops.arithmetic_operations as calculator

# 2. Import a specific function ('subtract') directly from the module
from Bookshops.arithmetic_operations import subtract

num1 = 5
num2 = 3

# To use the 'add' function, we must use the module's nickname
s = calculator.add(num1, num2)

# To use the 'subtract' function, we can call it directly
# because we imported it by name.
r = subtract(num1, num2)

print(f"The sum is: {s}")
print(f"The subtraction is: {r}")