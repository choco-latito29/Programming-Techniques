# --- File: lambda.py ---
# This file demonstrates 'lambda' functions,
# also known as anonymous functions.

# --- Example 1: Normal function vs. Lambda ---

# NORMAL function definition
def sum_normal(a, b):
    return a + b

# ANONYMOUS (LAMBDA) function definition
# 'lambda' creates a small function in one line.
# It can have multiple arguments, but only one expression.
sum_lambda = lambda a, b: a + b

# --- Example 2: Using a lambda function ---
sum_calc = lambda x, y: x + y

result = sum_calc(3, 5)
print(f"Result of lambda 3 + 5: {result}") # Output: 8

# --- Example 3: Passing a lambda function as an argument ---
# A normal function that takes another function as its argument
def high_order_function(lambda_func):
    # It calls the function it received with 2 and 4
    return lambda_func(2, 4)

# Call the high-order function, passing a lambda *as the argument*
result_2 = high_order_function(lambda a, b: a + b)
print(f"Result of passing lambda to function: {result_2}") # Output: 6

# --- Example 4: Calling a normal function from within a lambda ---
# A normal function
def normal_sum(a, b):
    return a + b

# A lambda that calls the normal function
result_3 = (lambda a, b: normal_sum(a, b))(2, 4)
print(f"Result of lambda calling normal function: {result_3}") # Output: 6