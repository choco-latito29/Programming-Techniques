# Author: YourLastNameFirstName (# is for a single-line comment)

"""
( Triple quotes are for
multi-line comments)
""" # Program Explanation

print('\n', "==== Basic Calculations ===", '\n') # Program Title

print("Enter your name: ") # Asks for the user's name
YourName = input() # Saves the user's name

base = float(input("Enter base: ")) # Asks for and saves the base

height = float(input("Enter height: ")) # Asks for and saves the height

Area = (base * height)/2 # Calculates the area of the triangle

print(f'\n{YourName} calculated the area: {Area}\n') # Shows the area result