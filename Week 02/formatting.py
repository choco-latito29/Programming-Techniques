from datetime import datetime # To work with dates and times
print("="*50) # Print a separator line
number = 11.5497 # Define a decimal number

# f-strings allow formatting inside the curly braces
print(f"With two decimals: {number:.2f}") # Shows the number with two decimals
print(f"Complete (float): {number:f}") # Shows the full number
print(f"Rounded: {round(number)}") # Rounds the number to the nearest integer
print(f"Number to string: {str(number)}") # Converts the number to a string

now = datetime.now() # Get the current date and time
print(f"Show current date: {now}") # Show the full datetime object

current_time = now.time() # Get only the time
print(f"Show current time: {current_time}") # Show the time

year = now.year # Get the current year
month = now.month # Get the current month
day = now.day # Get the current day

print(f"Show Year: {year}") # Show the year
print(f"Show Month: {month}") # Show the month
print(f"Show Day: {day}") # Show the day