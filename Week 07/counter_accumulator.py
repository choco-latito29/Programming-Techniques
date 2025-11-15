courseCounter = 0
creditAccumulator = 0

# Main program loop
while True:

    print("\n========== OPTIONS MENU ==========\n")
    print("1. Process")
    print("2. Report")
    print("3. Exit")

    # Menu validation loop
    while True:
        op = int(input("Enter an option: "))

        if (op < 1 or op > 3):
            print("[ERROR] Re-enter")
        else:
            break

    match op:
        case 1:
            courseName = input("Enter the course name: ")

            # 1. COUNTER: Increments by a fixed value (+1)
            courseCounter = courseCounter + 1

            # Credit validation loop
            while True:
                courseCredits = int(input(f"Enter credits (1 to 5) for the Course: "))

                # Corrected validation logic
                if (courseCredits < 1 or courseCredits > 5):
                    print("[ERROR] Credits must be between 1 and 5. Try again.")
                else:
                    break

            # 2. ACCUMULATOR: Increments by a variable value (the credits)
            creditAccumulator = creditAccumulator + courseCredits

        case 2:
            print("\n========== TOTAL REPORT ==========\n")
            print(f"The number of courses is: {courseCounter}")
            print(f"The total accumulated credits is: {creditAccumulator}")

        case 3:
            print("Exiting the program...")
            break