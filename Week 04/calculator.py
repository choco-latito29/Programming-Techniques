num1 = int(input("Enter the first number (a): ")) # Enter the first number.
operator = input("Enter the operator (+, -, *, /): ") # Enter the operator (Operation to perform)
num2 = int(input("Enter the second number (b): ")) # Enter the second number.

result = "" # Initialize an empty result.

if operator == "+": # Evaluate the operator and perform the corresponding operation.
    result = num1 + num2 # Perform the addition.
    print(f"{num1} + {num2} = {result}") # Print the result.
elif operator == "-": # Evaluate if the operator is subtraction.
    result = num1 - num2 # Perform the subtraction.
    print(f"{num1} - {num2} = {result}") # Print the result.
elif operator == "*": # Evaluate if the operator is multiplication.
    result = num1 * num2 # Perform the multiplication.
    print(f"{num1} * {num2} = {result}") # Print the result.
elif operator == "/": # Evaluate if the operator is division.
    if num2 != 0: # Verify that the divisor is not zero.
        result = num1 / num2 # Perform the division.
        print(f"{num1} / {num2} = {result}") # Print the result.
    else: # If the divisor is zero, show an error message.
        result = "Error: Division by zero"
        print(result)