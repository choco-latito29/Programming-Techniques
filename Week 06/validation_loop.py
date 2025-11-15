print("\n========== DATA ENTRY ==========\n")

# 1. This 'while True' loop will run indefinitely...
while True:
    # 'eval()' converts the string input (e.g., "3") into an integer (3)
    num = eval(input("Enter a number for a vowel (1-5): "))

    # 2. Validation check
    if (num < 1 or num > 5):
        print("[ERROR] Invalid number, please re-enter...")
    else:
        # 3. If the number is valid, 'break' exits the loop
        break

# 4. The 'match' statement only runs *after* the loop is broken
match num:
    case 1:
        print("It's vowel a")

    case 2:
        print("It's vowel e")

    case 3:
        print("It's vowel i")

    case 4:
        print("It's vowel o")

    case 5:
        print("It's vowel u")