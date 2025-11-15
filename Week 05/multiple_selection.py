print("\n========== DATA ENTRY ==========")

# 'eval()' will convert the user's input string "1" into the integer 1
num = eval(input("Enter a number for a vowel: "))

# The 'match' statement compares the 'num' variable...
match num:
    # ...to each 'case' until it finds a match.
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