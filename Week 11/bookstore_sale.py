# --- File: bookstore_sale.py ---
# This is the MAIN program for the Week 11 project.
# It imports and uses all the modules from the 'Bookshops' package
# to create a complete, menu-driven sales application.

# 1. Import all necessary modules with aliases
import Bookshops.utilities as util
import Bookshops.arithmetic_operations as calculator
import Bookshops.read_data as reader

# --- Global variables to store totals across multiple sales ---
male_count = 0
female_count = 0
total_client_count = 0
male_sales_over_1000 = 0
total_sales_accumulator = 0
female_sales_accumulator = 0


def print_report():
    """Prints the current status of all global counters and accumulators."""
    print("\n========== TOTAL REPORT ==========\n")
    print(f"Total number of clients: {total_client_count}")
    print(f"Number of female clients: {female_count}")
    print(f"Number of male clients: {male_count}")
    print(f"Male sales with total accumulated >= 1000: {male_sales_over_1000}")
    print(f"Total sales accumulator: {total_sales_accumulator}")
    print(f"Total sales accumulator for female clients: {female_sales_accumulator}")


def process_sale():
    """Handles the logic for a single sale and updates global variables."""
    # Notify Python that this function will MODIFY the global variables
    global male_count, female_count, total_client_count, male_sales_over_1000
    global total_sales_accumulator, female_sales_accumulator

    # --- 2. Use the 'reader' module to get validated input ---
    product_name = input("Enter the product name: ")
    product_price = reader.read_positive_float("Enter the product price: ")
    product_qty = reader.read_positive_int("Enter the product quantity: ")
    discount_percentage = reader.read_positive_float("Enter the discount percentage (e.g., 15): ")
    gender_upper = reader.read_gender("Enter the gender (M/F): ")

    # --- Business Logic ---
    match gender_upper:
        case 'M':
            male_count += 1
            bonus = 0.18
            # Logical Anomaly: This 'discount_rate' is calculated but never used
            if (product_qty <= 10):
                discount_rate = 0.2
            else:
                discount_rate = 0.5
        case 'F':
            female_count += 1
            bonus = 0.25
            # Logical Anomaly: This 'discount_rate' is calculated but never used
            if (product_qty <= 10):
                discount_rate = 0.3
            else:
                discount_rate = 0.4

    # --- 3. Use the 'calculator' module for math ---
    gross_amount = calculator.multiply(product_price, product_qty)
    bonus_amount = calculator.multiply(gross_amount, bonus)
    # The discount is correctly converted from % to decimal (e.g., 15 -> 0.15)
    discount_amount = calculator.multiply(gross_amount, discount_percentage / 100)

    # Calculate final payment
    temp_total = calculator.subtract(gross_amount, discount_amount)
    payment_amount = calculator.add(temp_total, bonus_amount)

    # --- 4. Update global accumulators ---
    total_client_count += 1
    total_sales_accumulator = calculator.add(total_sales_accumulator, payment_amount)

    if (gender_upper == 'F'):
        female_sales_accumulator += payment_amount

    if (gender_upper == 'M' and total_sales_accumulator >= 1000):
        male_sales_over_1000 += 1

    print("\n========== CLIENT REPORT ==========\n")
    print(f"Gross Amount: {gross_amount}")
    print(f"Bonus Amount: {bonus_amount}")
    print(f"Discount Amount: {discount_amount}")
    print(f"Amount to Pay: {payment_amount}")


def menu():
    """Displays the main menu and handles navigation."""
    print("\n========== MENU OPTIONS ==========\n")
    print("1. Process Sale")
    print("2. Run Report")
    print("3. Exit")

    # Use the 'reader' module to get a validated menu option
    op = reader.read_menu_option("Enter a menu option: ", 1, 3)

    match op:
        case 1:
            process_sale()
        case 2:
            print_report()
        case 3:
            # --- Exit Confirmation ---
            while True:
                response = input("Are you sure you want to exit? (Y/N): ")
                response_upper = response.upper()

                if (response_upper != 'S' and response_upper != 'N'):
                    print("[ERROR] Please re-enter")
                else:
                    break

            if (response_upper == 'S'):
                # 5. Use the 'util' module for the exit message
                util.exit_program()
            else:
                # If user selects 'N', set op to 0 to prevent the
                # main loop in executor() from breaking
                op = 0
    return op


def executor():
    """Main program loop."""
    while True:
        option = menu()
        # The program only exits if the user confirms 'S' in the menu,
        # which keeps 'option' as 3.
        if (option == 3):
            break


# --- Start the program ---
executor()