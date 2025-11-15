print("\n========== DATA ENTRY ==========")

# 'eval()' will convert the user's input string "3" into the integer 3
num = eval(input("Enter a number for a vowel: "))

# 1. Validation check: First, check if the number is in the valid range
if (num >= 1 and num <= 5):

    # 2. 'match' block: Only runs if the 'if' check passed
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
else:
    # 3. 'else' block: Runs if the 'if' check failed
    print("ERROR, you must enter a number from 1 to 5")