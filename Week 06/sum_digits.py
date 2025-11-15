# Initialize 'num' to 0 to ensure the validation loop runs at least once
num = 0

# 1. Validation Loop:
# This 'while' loop will continue to ask for a number
# as long as the number entered is 0 or negative.
while num <= 0:
    num = int(input("Enter a number: "))

    if (num <= 0):
        print("[ERROR] The number must be greater than 0... Try again")

# 2. Main Logic:
sum_of_digits = 0
processing_num = num  # Make a copy to work with, preserving the original 'num'

# This 'while' loop runs as long as there are digits left
while processing_num > 0:
    # Get the last digit using the modulo (%) operator
    digit = processing_num % 10

    # Add that digit to the sum
    sum_of_digits = sum_of_digits + digit

    # Remove the last digit using the integer division (//) operator
    processing_num = processing_num // 10

print("\n--- REPORT ---")
print(f"The entered number was: {num}")
print(f"The sum of its digits is: {sum_of_digits}")