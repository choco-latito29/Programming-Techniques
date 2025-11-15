# --- Global Counters and Accumulators ---
actionCounter = 0
categoryCCounter = 0
categoryECounter = 0
totalSolesAccumulator = 0
categoryBSolesAccumulator = 0
totalOver5kAccumulator = 0  # Logical Anomaly: This variable is never used.

# --- Initial data (set once) ---
baseAmount = int(input("Enter the base amount $: "))
exchangeRate = float(input("Enter the exchange rate $ => S: "))

# --- Main Program Loop ---
while True:
    print("\n========== OPTIONS MENU ==========\n")
    print("1. Calculate Taxes")
    print("2. Report Counters and Accumulators")
    print("3. Exit")

    # Menu Validation Loop
    while True:
        op = int(input("Enter an option: "))
        if (op < 1 or op > 3):
            print("[ERROR] Re-enter")
        else:
            break

    match op:
        case 1:
            # --- Sub-Menu Loop (runs once then breaks) ---
            while True:
                print("\n========== SUBMENU OPTIONS ==========\n")
                print("1. Category A")
                print("2. Category B")
                print("3. Category C")
                print("4. Category D")
                print("5. Category E")

                # Sub-Menu Validation Loop
                while True:
                    op = int(input("Enter a category: "))
                    if (op < 1 or op > 5):
                        print("[ERROR] Re-enter")
                    else:
                        break

                match op:
                    case 1:
                        actionCounter = actionCounter + 1
                        Category = "A"
                        vehicle = "Motorcycle"
                        taxRate = 0.3

                        taxAmount = baseAmount * taxRate
                        totalAmount = baseAmount + taxAmount
                        baseAmountSoles = baseAmount * exchangeRate
                        totalAmountSoles = totalAmount * exchangeRate

                        print("\n========== REGISTRATION REPORT ==========\n")
                        print(f"The category is: {Category}")
                        print(f"The vehicle type is: {vehicle}")
                        print(f"The base amount in soles is: {baseAmountSoles:.2f}")
                        print(f"The tax amount in soles is: {(baseAmountSoles * taxRate):.2f}")
                        print(f"The total amount to pay in soles is: {totalAmountSoles:.2f}")

                        totalSolesAccumulator = totalSolesAccumulator + totalAmountSoles
                        break

                    case 2:
                        actionCounter = actionCounter + 1
                        Category = "B"
                        vehicle = "Private Car"
                        taxRate = 0.5

                        taxAmount = baseAmount * taxRate
                        totalAmount = baseAmount + taxAmount
                        baseAmountSoles = baseAmount * exchangeRate
                        totalAmountSoles = totalAmount * exchangeRate

                        print("\n========== REGISTRATION REPORT ==========\n")
                        print(f"The category is: {Category}")
                        print(f"The vehicle type is: {vehicle}")
                        print(f"The base amount in soles is: {baseAmountSoles:.2f}")
                        print(f"The tax amount in soles is: {(baseAmountSoles * taxRate):.2f}")
                        print(f"The total amount to pay in soles is: {totalAmountSoles:.2f}")

                        totalSolesAccumulator = totalSolesAccumulator + totalAmountSoles
                        categoryBSolesAccumulator = categoryBSolesAccumulator + totalAmountSoles
                        break

                    case 3:
                        actionCounter = actionCounter + 1
                        categoryCCounter = categoryCCounter + 1
                        Category = "C"
                        vehicle = "SUV"
                        taxRate = 0.7

                        taxAmount = baseAmount * taxRate
                        totalAmount = baseAmount + taxAmount
                        baseAmountSoles = baseAmount * exchangeRate
                        totalAmountSoles = totalAmount * exchangeRate

                        print("\n========== REGISTRATION REPORT ==========\n")
                        print(f"The category is: {Category}")
                        print(f"The vehicle type is: {vehicle}")
                        print(f"The base amount in soles is: {baseAmountSoles:.2f}")
                        print(f"The tax amount in soles is: {(baseAmountSoles * taxRate):.2f}")
                        print(f"The total amount to pay in soles is: {totalAmountSoles:.2f}")

                        totalSolesAccumulator = totalSolesAccumulator + totalAmountSoles
                        break

                    case 4:
                        actionCounter = actionCounter + 1
                        Category = "D"
                        vehicle = "Truck"
                        taxRate = 0.10

                        taxAmount = baseAmount * taxRate
                        totalAmount = baseAmount + taxAmount
                        baseAmountSoles = baseAmount * exchangeRate
                        totalAmountSoles = totalAmount * exchangeRate

                        print("\n========== REGISTRATION REPORT ==========\n")
                        print(f"The category is: {Category}")
                        print(f"The vehicle type is: {vehicle}")
                        print(f"The base amount in soles is: {baseAmountSoles:.2f}")
                        print(f"The tax amount in soles is: {(baseAmountSoles * taxRate):.2f}")
                        print(f"The total amount to pay in soles is: {totalAmountSoles:.2f}")

                        totalSolesAccumulator = totalSolesAccumulator + totalAmountSoles
                        break

                    case 5:
                        actionCounter = actionCounter + 1
                        categoryECounter = categoryECounter + 1
                        Category = "E"
                        vehicle = "Trailer"
                        taxRate = 0.12

                        taxAmount = baseAmount * taxRate
                        totalAmount = baseAmount + taxAmount
                        baseAmountSoles = baseAmount * exchangeRate
                        totalAmountSoles = totalAmount * exchangeRate

                        print("\n========== REGISTRATION REPORT ==========\n")
                        print(f"The category is: {Category}")
                        print(f"The vehicle type is: {vehicle}")
                        print(f"The base amount in soles is: {baseAmountSoles:.2f}")
                        print(f"The tax amount in soles is: {(baseAmountSoles * taxRate):.2f}")
                        print(f"The total amount to pay in soles is: {totalAmountSoles:.2f}")

                        totalSolesAccumulator = totalSolesAccumulator + totalAmountSoles
                        break

        case 2:
            print("\n========== TOTAL REPORT ==========\n")
            print(f"The number of actions performed is: {actionCounter}")
            print(f"The accumulated count for C is: {categoryCCounter}")
            print(f"The total amount to pay in soles is: {totalSolesAccumulator:.2f}")
            print(f"The total amount to pay in soles for category B is: {categoryBSolesAccumulator:.2f}")
            print(f"Accumulated amount for totals > 5000 is: {totalOver5kAccumulator}")

        case 3:
            print("Exiting the program...")
            break