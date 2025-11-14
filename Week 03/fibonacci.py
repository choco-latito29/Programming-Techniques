a = 1  # First value of the series
b = 1  # Second value of the series

print("\n========== DATA ENTRY ==========\n")  # Program Title

limit = int(input("Enter the limit: "))  # Request the limit

print(f"The Fibonacci series is: {a}")

while (b <= limit):  # While b is less than or equal to the limit
    print(b)  # Show the value of b
    c = a + b  # Calculate the sum of a and b
    a = b  # Update the value of a
    b = c  # Update the value of b

print("\n========== END OF PROGRAM ==========\n")  # End of program