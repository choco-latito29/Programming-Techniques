print("\n***Example 6: Using eval()****\n") # Program Title

# eval() interprets the input string as Python code.
# If the user types "10", eval() runs it and gets the integer 10.
variable1 = eval(input("Enter the value of variable a: "))
variable2 = eval(input("Enter the value of variable b: "))

# Because the variables are now numbers, the '+' operator performs addition
variable3 = variable1 + variable2

print(f"The result is: {variable3}")
print(f"The result as a string is: {str(variable3)}")