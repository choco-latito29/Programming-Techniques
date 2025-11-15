print("\n========== DATA ENTRY ==========")

num = int(input("Enter an integer: "))

# 1. First (outer) check: Is the number positive?
if (num > 0):

    # 2. Second (nested) check: Is it in the 1-10 range?
    if (num >= 1 and num <= 10):
        print("It is in the range of the first ten numbers.")
    else:
        # Runs if the number is greater than 10
        print("It is beyond the range of the first ten numbers.")
else:
    # Runs if the number is not greater than zero (i.e., 0 or negative)
    print("[ERROR] The number is not greater than zero.")