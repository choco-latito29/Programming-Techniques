balance = 0

print("\n========== ATM MENU ==========")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

menuOption = int(input("Enter an option: "))

# 1. Outer validation 'if'
if (menuOption >= 1 and menuOption <= 4):

    # 2. 'match' block for valid options
    match menuOption:
        case 1:
            depositAmount = float(input("Enter the amount to Deposit: "))

            # 3. Nested validation for deposit
            if depositAmount > 0:
                balance = balance + depositAmount
            else:
                print("[ERROR] The deposit amount must be greater than 0")

        case 2:
            withdrawalAmount = float(input("Enter the amount to withdraw: "))

            # 4. Nested validation for withdrawal
            if withdrawalAmount > 0:
                # 5. Deeper nested validation for sufficient funds
                if withdrawalAmount <= balance:
                    balance = balance - withdrawalAmount
                else:
                    print("----- INSUFFICIENT BALANCE -----")
            else:
                print("[ERROR] The withdrawal amount must be greater than 0")

        case 3:
            print(f"Your current balance is: {balance}")

        case 4:
            print("Thank you---- Come again soon")
else:
    # 6. 'else' block for the outer validation
    print("[ERROR] Please enter a valid number")