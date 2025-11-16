# --- File: recursive_sales_menu.py ---
# This program demonstrates a complex sales menu that uses
# global variables, nested validation loops, and a
# RECURSIVE call in the menu logic.

# --- Global Counters and Accumulators ---
global male_count, female_count, total_client_count, male_sales_over_1000
global total_sales_accumulator, female_sales_accumulator
male_count = 0
female_count = 0
total_client_count = 0
male_sales_over_1000 = 0
total_sales_accumulator = 0
female_sales_accumulator = 0


def exit_program():
    """Prints the exit message."""
    print("Thank you, come again soon..!")


def print_report():
    """Prints the current value of all global counters and accumulators."""
    print("\n======== TOTAL REPORT ==========\n")
    print(f"Total Client count is: {total_client_count}")
    print(f"Female Client count is: {female_count}")
    print(f"Male Client count is: {male_count}")
    print(f"Male Client sales (accumulated > 1000) is: {male_sales_over_1000}")
    print(f"Total Sales accumulator is: {total_sales_accumulator}")
    print(f"Total Sales accumulator for Female Clients is: {female_sales_accumulator}")


def process_sale():
    """Gets all user data, calculates the sale, and updates global variables."""
    # Declares which global variables will be MODIFIED
    global male_count, female_count, total_client_count, male_sales_over_1000
    global total_sales_accumulator, female_sales_accumulator

    product_name = input("Enter Product Name: ")

    # --- Price Validation Loop ---
    while True:
        product_price = float(input("Enter Product Price: "))
        if (product_price <= 0):
            print("[ERROR]. Re-enter")
        else:
            break

    # --- Quantity Validation Loop ---
    while True:
        product_qty = int(input("Enter Product Quantity: "))
        if (product_qty <= 0):
            print("[ERROR]. Re-enter")
        else:
            break

    # --- Discount % Validation Loop ---
    while True:
        discount_percentage = float(input("Enter Discount Percentage: "))
        if (discount_percentage <= 0):
            print("[ERROR]. Re-enter")
        else:
            break

    # --- Gender Validation Loop ---
    while True:
        gender = (input("Enter Gender: "))
        gender_upper = gender.upper()
        if (gender_upper != 'F' and gender_upper != 'M'):
            print("[ERROR]. Re-enter")
        else:
            break

    # Determine bonus and (unused) discount rate
    match gender_upper:
        case 'M':
            male_count = male_count + 1
            bonus = 0.18
            if (product_qty <= 10):
                discount_rate = 0.2
            else:
                discount_rate = 0.5

        case 'F':
            female_count = female_count + 1
            bonus = 0.25
            if (product_qty <= 10):
                discount_rate = 0.3
            else:
                discount_rate = 0.4

    # --- Calculations ---
    gross_amount = product_price * product_qty
    bonus_amount = gross_amount * bonus

    # --- Logical Anomaly 1: This uses the raw percentage (e.g., 15)
    # --- not the decimal (e.g., 0.15) for calculation.
    discount_amount = gross_amount * discount_percentage

    # --- Logical Anomaly 2: The 'discount_rate' (0.2, 0.5, etc.)
    # --- calculated in the 'match' block is never used.

    payment_amount = gross_amount - discount_amount + bonus_amount

    # --- Update Global Accumulators ---
    total_client_count = total_client_count + 1
    total_sales_accumulator = total_sales_accumulator + payment_amount

    if (gender_upper == 'F'):
        female_sales_accumulator = female_sales_accumulator + payment_amount

    if (gender_upper == 'M' and total_sales_accumulator >= 1000):
        male_sales_over_1000 = male_sales_over_1000 + 1

    # --- Print Per-Client Report ---
    print("\n=========== CLIENT REPORT ===========\n")
    print(f"The Gross Amount is: {gross_amount}")
    print(f"The Bonus Amount is: {bonus_amount}")
    print(f"The Discount Amount is: {discount_amount}", )
    print(f"The Amount to Pay is: {payment_amount}")


def menu():
    """Handles the main menu logic and navigation."""
    print("\n======== MENU OPTIONS ==========\n")
    print("1. Process")
    print("2. Report")
    print("3. Exit")

    # --- Menu Validation Loop ---
    while True:
        op = int(input("Enter menu option: "))
        if (op < 1 or op > 3):
            print("[ERROR]. Re-enter")
        else:
            break

    match op:
        case 1:
            process_sale()

        case 2:
            print_report()

        case 3:
            # --- Exit Confirmation Loop ---
            while True:
                response = input("Are you sure you want to exit? (Y/N):")
                response_upper = response.upper()

                if (response_upper != 'S' and response_upper != 'N'):
                    print("[ERROR]. Re-enter")
                else:
                    break

            if (response_upper == 'S'):
                exit_program()
            else:
                # --- RECURSIVE CALL ---
                # If the user chooses 'N', the menu() function calls itself
                # to show the menu again.
                menu()

    return op;


def executor():
    """Main program loop."""
    while True:
        # Get the option from the menu
        option = menu()

        # The 'executor' loop ONLY breaks if the user
        # confirms 'Yes' to exit (which makes 'option' == 3)
        if (option == 3):
            break


# --- Start the program ---
executor()