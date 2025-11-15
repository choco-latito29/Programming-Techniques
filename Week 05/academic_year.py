print("\n========== ACADEMIC PROGRESS LEVEL ==========\n")

credits = int(input("Enter the amount of accumulated credits: "))

# 1. First, check if the credits are a positive number
if (credits >= 0):

    # 2. Second, check if credits are within the valid range (<= 160)
    if (credits <= 160):

        academic_year = ""  # Initialize an empty string

        # 3. Chained conditional to find the correct year
        if credits < 32:
            academic_year = "First Year"
        elif credits <= 63:
            academic_year = "Second Year"
        elif credits <= 95:
            academic_year = "Third Year"
        elif credits <= 127:
            academic_year = "Fourth Year"
        else:  # If it's 128 or more (up to 160)
            academic_year = "Fifth Year"

        print(f"Academic Year: {academic_year}")

    else:
        # This 'else' belongs to the second check (credits <= 160)
        print("[Error] The amount of credits cannot be more than 160.")
else:
    # This 'else' belongs to the first check (credits >= 0)
    print("[Error] The amount of credits must be a positive number.")