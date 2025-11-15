balance = 0

# 1. Main Program Loop (keeps the main menu running)
while True:
    print("\n======== Main Menu ==========")
    print("1. Process")
    print("2. Exit")

    # 2. Validation loop for main menu input
    while True:
        menuOption = int(input("Enter menu option: "))

        if (menuOption < 1 or menuOption > 2):
            print("ERROR. Re-enter 1 or 2")
        else:
            break

    match menuOption:
        case 1:
            # 3. Sub-Menu Loop (keeps the sub-menu running)
            while True:
                print("\n======== ATM SUB-MENU ==========")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Back")

                # 4. Validation loop for sub-menu input
                while True:
                    subMenuOption = int(input("Enter menu option: "))

                    if (subMenuOption < 1 or subMenuOption > 4):
                        print("[ERROR] Re-enter 1, 2, 3, or 4")
                    else:
                        break

                match subMenuOption:
                    case 1:
                        # 5. Validation loop for deposit amount
                        while True:
                            depositAmount = float(input("Enter Amount to Deposit: "))

                            if (depositAmount <= 0):
                                print("[ERROR] Re-enter, deposit amount must be > 0")
                            else:
                                break
                        balance = balance + depositAmount

                    case 2:
                        # 6. Validation loop for withdrawal amount
                        while True:
                            withdrawalAmount = float(input("Enter Amount to Withdraw: "))

                            if (withdrawalAmount <= 0):
                                print("[ERROR] Re-enter, withdrawal amount must be > 0")
                            else:
                                break

                        if withdrawalAmount <= balance:
                            balance = balance - withdrawalAmount
                        else:
                            print("---------- Insufficient Balance. -------------")

                    case 3:
                        print(f"Your current balance is: {balance}")

                    case 4:
                        # 7. Validation loop for sub-menu exit confirmation
                        while True:
                            subConfirm = input("Are you sure you want to go back? (Y/N): ")
                            subConfirmUpper = subConfirm.upper()

                            if (subConfirmUpper != "Y" and subConfirmUpper != "N"):
                                print("[ERROR] Re-enter Y or N")
                            else:
                                break

                        if subConfirmUpper == "Y":
                            print("Returning to Main Menu...")
                            # 8. This 'break' exits the Sub-Menu Loop (3)
                            break

        case 2:
            # 9. Validation loop for main menu exit confirmation
            while True:
                mainConfirm = input("Are you sure you want to Exit? (Y/N): ")
                mainConfirmUpper = mainConfirm.upper()

                if (mainConfirmUpper != "Y" and mainConfirmUpper != "N"):
                    print("[ERROR] Re-enter Y or N")
                else:
                    break

            if mainConfirmUpper == "Y":
                print("[Thank you] Come again soon..!")
                # 10. This 'break' exits the Main Program Loop (1)
                break