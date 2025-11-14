print("\nExample 1: String (Character) Usage\n")

# This code demonstrates a common TypeError.
# 'variable1' and 'variable2' are saved as strings (text), not numbers.
variable1 = '9'
variable2 = '5'

# Python cannot multiply two strings together.
# This line will intentionally cause an error to show the concept.
variable3 = variable1 * variable2

print(f"The result is: {variable3}")