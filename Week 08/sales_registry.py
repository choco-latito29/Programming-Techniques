# --- Global Counters and Accumulators ---
female_client_count = 0
sales_100_to_1000_count = 0
male_client_sales_count = 0
total_sales_accumulator = 0

# --- Report-specific variables ---
sales = []  # List to store each sale as a dictionary
vip_amount_accumulator = 0
male_net_amount_accumulator = 0
regular_client_count = 0
regular_amount_accumulator = 0
best_client = None
highest_amount = 0

# --- Main Program Loop ---
while True:
    print("\n========== MAIN MENU ==========\n")
    print("1. Register Sale")
    print("2. Sales Report")
    print("3. Exit")

    # --- Menu Validation Loop ---
    while True:
        op = int(input("Enter a menu option: "))
        if op < 1 or op > 3:
            print("[ERROR] Re-enter")
        else:
            break

    match op:
        case 1:
            # --- Data Validation Loop ---
            while True:
                print("\n========== CLIENT TYPE ==========\n")
                print("1. Regular")
                print("2. VIP")
                client_type = int(input("Select client type (1-Regular, 2-VIP): "))
                if client_type not in [1, 2]:
                    print("[ERROR] Invalid client type.")
                    continue  # Restarts the validation loop

                gender = input("Enter client gender (M/F): ").strip().upper()
                if gender not in ["M", "F"]:
                    print("[ERROR] Invalid gender.")
                    continue

                print("\n========== PLAN TYPE ==========\n")
                print("1. Basic (S/ 100 per month)")
                print("2. Plus (S/ 200 per month)")
                print("3. Elite (S/ 300 per month)")
                plan_type = int(input("Select plan type (1-Basic, 2-Plus, 3-Elite): "))
                if plan_type not in [1, 2, 3]:
                    print("[ERROR] Invalid plan type.")
                    continue

                months = int(input("Enter number of membership months: "))
                if months < 1:
                    print("[ERROR] Invalid number of months.")
                    continue

                # --- Calculations ---
                prices = {1: 100, 2: 200, 3: 300}
                base_price = prices[plan_type] * months

                # Discounts
                if months == 1:
                    discount = 0
                elif 2 <= months <= 5:
                    discount = 0.05
                elif 6 <= months <= 10:
                    discount = 0.10
                else:  # 11 or more months
                    discount = 0.15

                net_amount = base_price * (1 - discount)

                # Store the sale as a dictionary
                sale = {
                    "client_type": client_type,
                    "gender": gender,
                    "plan_type": plan_type,
                    "months": months,
                    "net_amount": net_amount
                }
                sales.append(sale)

                # --- Accumulators and Counters (LOGIC CORRECTED) ---
                total_sales_accumulator += net_amount

                if 100 <= net_amount <= 1000:
                    sales_100_to_1000_count += 1

                if gender == "F":
                    female_client_count += 1
                elif gender == "M":
                    male_client_sales_count += 1
                    male_net_amount_accumulator += net_amount

                if client_type == 2:
                    vip_amount_accumulator += net_amount

                if client_type == 1:
                    regular_client_count += 1
                    regular_amount_accumulator += net_amount

                # Find the best client (highest sale)
                if net_amount > highest_amount:
                    highest_amount = net_amount
                    best_client = sale

                print(f"Sale registered. Net amount: S/ {net_amount:.2f}")
                # If all validations pass, exit the validation loop
                break

        case 2:
            print("\n========== SALES REPORT ==========\n")
            print(f"Number of female clients: {female_client_count}")
            print(f"Number of sales between S/ 100 and S/ 1000: {sales_100_to_1000_count}")
            print(f"Number of sales to male clients: {male_client_sales_count}")
            print(f"Total accumulator for all sales: S/ {total_sales_accumulator:.2f}")
            print(f"Net amount accumulator for type 2 (VIP): S/ {vip_amount_accumulator:.2f}")

            if regular_client_count > 0:
                average_regular = regular_amount_accumulator / regular_client_count
            else:
                average_regular = 0

            print(f"Average net amount for regular clients: S/ {average_regular:.2f}")

            if best_client:
                # Look up the plan name from a list using the plan_type index
                plan_names = ['Basic', 'Plus', 'Elite']
                client_type_name = 'Regular' if best_client['client_type'] == 1 else 'VIP'
                plan_name = plan_names[best_client['plan_type'] - 1]

                print(
                    f"Highest sale (best client): Amount S/ {highest_amount:.2f}, Client Type: {client_type_name}, Gender: {best_client['gender']}, Plan: {plan_name}, Months: {best_client['months']}")
            else:
                print("No sales registered yet.")

        case 3:
            print("[COME AGAIN SOON] Exiting program.........")
            break  # This break exits the main program loop