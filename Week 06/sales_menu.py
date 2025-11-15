while True:

    print("\n=========== MENU OPTIONS =============\n")
    print("1. Make Sale")
    print("2. Exit")

    # --- Menu Validation Loop ---
    while True:
        op = int(input(("Enter menu option: ")))

        if (op < 1 or op > 2):
            print("ERROR. Re-enter")
        else:
            break

    match op:
        case 1:
            productName = input("Enter Product Name: ")

            # --- Price Validation Loop ---
            while True:
                productPrice = float(input("Enter Product Price: "))
                if (productPrice <= 0):
                    print("[ERROR] Re-enter")
                else:
                    break

            # --- Quantity Validation Loop ---
            while True:
                productQty = int(input("Enter Product Quantity: "))
                if (productQty <= 0):
                    print("ERROR. Re-enter")
                else:
                    break

            # --- Discount Validation Loop ---
            while True:
                discountPercentage = float(input("Enter Discount Percentage: "))
                if (discountPercentage <= 0):
                    print("ERROR. Re-enter")
                else:
                    break

            # --- Gender Validation Loop ---
            while True:
                gender = (input("Enter Gender (M/F): "))
                genderUpper = gender.upper()
                if (genderUpper != 'F' and genderUpper != 'M'):
                    print("[ERROR] Re-enter")
                else:
                    break

            match genderUpper:
                case 'M':
                    bonus = 0.18
                    if (productQty <= 10):
                        discount_rate = 0.2
                    else:
                        discount_rate = 0.5
                case 'F':
                    bonus = 0.25
                    if (productQty <= 10):
                        discount_rate = 0.3
                    else:
                        discount_rate = 0.4

            # --- Calculations ---
            grossAmount = productPrice * productQty
            bonusAmount = grossAmount * bonus

            # --- Logical Anomaly 1: The 'discountPercentage' (e.g., 15) is used directly
            # --- instead of 'discountPercentage / 100' (e.g., 0.15)
            discountAmount = grossAmount * discountPercentage

            # --- Logical Anomaly 2: The 'discount_rate' (0.2, 0.5, etc.)
            # --- is calculated but never used.

            paymentAmount = grossAmount - discountAmount + bonusAmount

            print("\n=========== REPORT =============\n")
            print(f"The Gross Amount is: {grossAmount}")
            print(f"The Bonus Amount is: {bonusAmount}")
            print(f"The Discount Amount is: {discountAmount}")
            print(f"The Amount to Pay is: {paymentAmount}")

        case 2:
            print("Thank you, come again soon..!")
            # This 'break' exits the main 'while True' loop
            break