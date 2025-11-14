print("\n****Example 5: Using Input****\n")

# By default, values from input() are saved as strings (text).
variable1 = input("Enter the value of variable a: ") # input() receives text
variable2 = input("Enter the value of variable b: ") # input() receives text

# Because they are strings, the '+' operator concatenates them, it does not add them.
variable3 = variable1 + variable2

print(f"The result is: {variable3}")