while True:

    print("\n========== MAIN MENU ==========")
    print("1. Process")
    print("2. Exit")

    # --- Main Menu Validation Loop ---
    while True:
        menuOption = int(input("Enter menu option: "))

        if (menuOption < 1 or menuOption > 2):
            print("ERROR. Re-enter 1 or 2")
        else:
            break

    match menuOption:

        case 1:
            # --- Sub-Menu Loop ---
            while True:
                print("\n------ TOURIST DESTINATIONS SUB-MENU ------")
                print("1. Punta Cana")
                print("2. San Andrés")
                print("3. Cancún")
                print("4. Back")

                # --- Sub-Menu Validation Loop ---
                while True:
                    subMenuOption = int(input("Enter menu option: "))

                    if (subMenuOption < 1 or subMenuOption > 4):
                        print("[ERROR] Re-enter 1, 2, 3, or 4")
                    else:
                        break

                match subMenuOption:
                    case 1:  # Punta Cana
                        # --- Input Validation Loop ---
                        while True:
                            personCount = int(input("Enter the number of people: "))
                            if (personCount <= 0):
                                print("[ERROR] The amount must be greater than zero.")
                            else:
                                break
                        # --- Input Validation Loop ---
                        while True:
                            exchangeRate = float(input("Enter the day's exchange rate: "))
                            if (exchangeRate <= 0):
                                print("[ERROR] The exchange rate must be a positive value.")
                            else:
                                break

                        price_usd = 780
                        discount_percentage = 0.035
                        subtotal_usd = price_usd * personCount
                        discount_amount_usd = 0

                        if (personCount > 4):
                            discount_amount_usd = subtotal_usd * discount_percentage

                        total_usd = subtotal_usd - discount_amount_usd
                        total_soles = total_usd * exchangeRate

                        print(f"The total to pay is: {total_soles:.2f} soles")

                    case 2:  # San Andrés
                        # --- Input Validation Loop ---
                        while True:
                            personCount = int(input("Enter the number of people: "))
                            if (personCount <= 0):
                                print("[ERROR] The amount must be greater than zero.")
                            else:
                                break
                        # --- Input Validation Loop ---
                        while True:
                            exchangeRate = float(input("Enter the day's exchange rate: "))
                            if (exchangeRate <= 0):
                                print("[ERROR] The exchange rate must be a positive value.")
                            else:
                                break

                        price_usd = 1350
                        discount_percentage = 0.04
                        subtotal_usd = price_usd * personCount
                        discount_amount_usd = 0

                        if (personCount > 4):
                            discount_amount_usd = subtotal_usd * discount_percentage

                        total_usd = subtotal_usd - discount_amount_usd
                        total_soles = total_usd * exchangeRate

                        print(f"The total to pay is: {total_soles:.2f} soles")

                    case 3:  # Cancún
                        # --- Input Validation Loop ---
                        while True:
                            personCount = int(input("Enter the number of people: "))
                            if (personCount <= 0):
                                print("[ERROR] The amount must be greater than zero.")
                            else:
                                break
                        # --- Input Validation Loop ---
                        while True:
                            exchangeRate = float(input("Enter the day's exchange rate: "))
                            if (exchangeRate <= 0):
                                print("[ERROR] The exchange rate must be a positive value.")
                            else:
                                break

                        price_usd = 2550
                        discount_percentage = 0.045
                        subtotal_usd = price_usd * personCount
                        discount_amount_usd = 0

                        if (personCount > 4):
                            discount_amount_usd = subtotal_usd * discount_percentage

                        total_usd = subtotal_usd - discount_amount_usd
                        total_soles = total_usd * exchangeRate

                        print(f"The total to pay is: {total_soles:.2f} soles")

                    case 4:  # Back to Main Menu
                        # --- Confirmation Loop ---
                        while True:
                            confirm = input("Are you sure you want to go back? (Y/N): ")
                            confirmUpper = confirm.upper()

                            if (confirmUpper != "S" and confirmUpper != "N"):
                                print("[ERROR] Re-enter Y or N")
                            else:
                                break

                        if confirmUpper == "S":
                            print("Returning to Main Menu...")
                            # This 'break' exits the Sub-Menu Loop
                            break

        case 2:  # Exit Main Menu
            # --- Confirmation Loop ---
            while True:
                confirm = input("Are you sure you want to Exit? (Y/N): ")
                confirmUpper = confirm.upper()

                if (confirmUpper != "S" and confirmUpper != "N"):
                    print("[ERROR] Re-enter Y or N")
                else:
                    break

            if confirmUpper == "S":
                print("[Thank you] Come again soon..!")
                # This 'break' exits the Main Program Loop
                break