a = 0
b = 1

print("\n========== DATA ENTRY ==========\n")

limit = int(input("Enter the limit: "))

print(f"The Fibonacci series is: {a}")

while (b <= limit):
    print(b)
    c = a + b
    a = b
    b = c