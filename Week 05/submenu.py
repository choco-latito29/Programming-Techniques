balance = 0

print("\n========== MAIN MENU ==========")
print("1. Process")
print("2. Exit")

menuOption = int(input("Enter an option: "))

# 1. Main Menu Validation
if (menuOption >= 1 and menuOption <= 2):

    match menuOption:
        case 1:
            # --- Start of Sub-Menu ---
            print("\n========== ATM SUB-MENU ==========")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            subMenuOption = int(input("Enter an option: "))

            # 2. Sub-Menu Validation (Nested)
            if (subMenuOption >= 1 and subMenuOption <= 4):

                # 3. Sub-Menu Logic (Nested 'match')
                match subMenuOption:
                    case 1:
                        depositAmount = float(input("Enter the amount to Deposit: "))

                        if depositAmount > 0:
                            balance = balance + depositAmount
                        else:
                            print("[ERROR] The deposit amount must be greater than 0")

                    case 2:
                        withdrawalAmount = float(input("Enter the amount to withdraw: "))

                        if withdrawalAmount > 0:
                            if withdrawalAmount <= balance:
                                balance = balance - withdrawalAmount
                            else:
                                print("----- INSUFFICIENT BALANCE -----")
                        else:
                            print("[ERROR] The withdrawal amount must be greater than 0")

                    case 3:
                        print(f"Your current balance is: {balance}")

                    case 4:
                        print("Returning to main menu")  # (In this script, the program just ends)
            else:
                # 'else' for the Sub-Menu Validation
                print("[ERROR] Please enter a valid number [1 & 2 & 3 & 4]")
            # --- End of Sub-Menu ---

        case 2:
            print("Thank you---- Come again soon")
else:
    # 4. 'else' for the Main Menu Validation
    print("[ERROR] Please enter a valid number [1 & 2]")