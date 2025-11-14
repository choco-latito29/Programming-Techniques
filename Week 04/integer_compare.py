print("\n========== DATA ENTRY ==========\n") # Program Title

a = int(input("Enter the first number (a): ")) # Input for the first number
b = int(input("Enter the second number (b): ")) # Input for the second number
c = int(input("Enter the third number (c): ")) # Input for the third number

print("\n========== REPORT ==========\n") # Report Title

if a == b == c: # Checks if all three numbers are equal
    print("All three numbers are equal.") # Message if all three are equal
else: # If they are not all equal, find the largest
    largest = a # Assume 'a' is the largest initially

    if b > largest: # Check if 'b' is larger than the current largest
        largest = b # Update largest to 'b'
    if c > largest: # Check if 'c' is larger than the current largest
        largest = c # Update largest to 'c'

    # Check for ties between two numbers
    if largest == a and largest == b:
        print(f"The largest are A and B = {largest}")
    elif largest == a and largest == c:
        print(f"The largest are A and C = {largest}")
    elif largest == b and largest == c:
        print(f"The largest are B and C = {largest}")
    # Check for a single largest number
    elif largest == a:
        print(f"The largest is A = {largest}")
    elif largest == b:
        print(f"The largest is B = {largest}")
    else: # If none of the above, 'c' must be the largest
        print(f"The largest is C = {largest}")