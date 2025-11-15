product = 1

print("="*50)

n = int(input("Enter the number for factorial: "))

# range(n) creates a sequence from 0 to n-1
for i in range(n):
    # 'i' starts at 0, so we add 1 to get the sequence 1, 2, 3...
    i = i + 1
    product = product * i

print("\n========== REPORT ==========\n")
print(f"The factorial of {n} is {product}")