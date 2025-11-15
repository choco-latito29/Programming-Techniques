balance = 0

# 1. This is the main program loop. It will run forever.
while True:

    print("\n========== ATM MENU ==========\n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    # 2. This is a nested validation loop for the menu option.
    while True:
        menuOption = int(input("Enter a menu option: "))
        if (menuOption < 1 or menuOption > 4):
            print("[ERROR] Please re-enter....")
        else:
            break  # Exits the validation loop

    match menuOption:

        case 1:
            # 3. This is a nested validation loop for the deposit amount.
            while True:
                depositAmount = float(input("Enter amount to deposit: "))
                if (depositAmount <= 0):
                    print("[ERROR] Please re-enter the amount")
                else:
                    balance = balance + depositAmount
                    break  # Exits the deposit validation loop

        case 2:
            # 4. This is a nested validation loop for the withdrawal amount.
            while True:
                withdrawalAmount = float(input("Enter amount to withdraw: "))
                if (withdrawalAmount <= 0):
                    print("[ERROR] Please re-enter the amount")
                else:
                    if withdrawalAmount <= balance:
                        balance = balance - withdrawalAmount
                    else:
                        print("------------ Insufficient Balance ------------")
                    break  # Exits the withdrawal validation loop

        case 3:
            print(f"Your current balance is: {balance}")

        case 4:
            print("[Thank you] Come again soon...")
            # 5. This 'break' exits the MAIN program loop.
            break