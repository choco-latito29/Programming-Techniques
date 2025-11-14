import math # Import the math library

print('\n', "==== Equations ===", '\n') # Program Title

# Get user input. float() is safer than eval()
x = float(input("Enter the value of x: "))

# Calculate (x + 3) squared.
# Note: pow() is a built-in Python function.
power1 = pow(x + 3, 2)

# Calculate the square root of (x + 5)
sqrt_val = math.sqrt(x + 5)

# Calculate x raised to the power of 2/3
power2 = pow(x, 2/3)

# Calculate the final value of z using the formula
z = (power1 + x + sqrt_val) / power2 + 1

print(f"\nThe result of the equation is: {z}\n")