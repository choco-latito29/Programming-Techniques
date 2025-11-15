print("\n========== DATA ENTRY ==========")

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# This is a compound conditional structure (if-else)
if (a > 0 and b > 0):
    c = a + b
    print(f"The value of the sum is: {c}")
else:
    c = a * b
    print(f"The value of the multiplication is: {c}")