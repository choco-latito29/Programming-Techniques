print("\n========== DATA ENTRY ==========")

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))
num3 = int(input("Enter an integer: "))

if (num1 >= num2 and num1 >= num3):
    largest = num1
elif (num2 >= num1 and num2 <= num3): # <-- Logical Error 1
        largest = num2
        print("It is in the range of the first ten numbers") # <-- Logical Error 2
elif (num3 >= num1 and num3 >= num2):
        largest = num3

# This line will cause an UnboundLocalError if no condition is met
print(f"The largest number is: {largest}")