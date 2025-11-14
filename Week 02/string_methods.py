# a) Concatenation
print("="*50) # Print a separator line
firstName = input("Enter the person's first name: ") # Get the first name
lastName = input("Enter the person's last name: ") # Get the last name

fullName = firstName + " " + lastName # Concatenate the first and last name

print("="*50) # Print a separator line
print(f"Full name: {fullName}") # Show the full name

# b) Length of string
print("="*50) # Print a separator line
print(f"String length: {len(fullName)}") # Show the length of the string

# c) String Slicing
print("="*50) # Print a separator line
print("\nExtract first two letters") # Show message
# Slice from position 0 (first letter) up to (but not including) position 2
print(f"{fullName[0:2]}") # Show the first two letters

# d) String Membership
print("="*50) # Print a separator line
print(f"'j' in fullName: {'j' in (fullName)}") # Check if 'j' is in the full name
print(f"'ab' in fullName: {'ab' in fullName}") # Check if 'ab' is in the full name

# e) Case Methods
print("="*50) # Print a separator line
firstLetterUpper = fullName.capitalize() # Capitalize the first letter
print(f"First letter uppercase: {firstLetterUpper}") # Show the result

allUpper = fullName.upper() # Convert everything to uppercase
print(f"All Uppercase: {allUpper}") # Show the result

allLower = fullName.lower() # Convert everything to lowercase
print(f"All Lowercase: {allLower}") # Show the result