# --- File: electricity_app.py ---
# This is the MAIN program for the Electricity Consumption Control system.
# It imports the modules from the 'Bookshops' package.

import Bookshops.data_input as reader
import Bookshops.utilities as util
import Bookshops.rates as rates

# --- Global Counters and Accumulators ---
total_bills = 0
count_category_A = 0
count_category_C = 0
accum_total_pay = 0.0
accum_high_bills = 0.0  # For bills >= 600


def print_report():
    """Prints the statistical report of all processed bills."""
    print("\n======== GENERAL REPORT ========")
    print(f"Total number of bills calculated: {total_bills}")
    print(f"Count of Category 'A': {count_category_A}")
    print(f"Count of Category 'C': {count_category_C}")
    print(f"Accumulated total amount to pay: S/ {accum_total_pay:.2f}")
    print(f"Accumulated amounts >= S/ 600: S/ {accum_high_bills:.2f}")
    print("=" * 35)


def process_bill():
    """Handles data entry, calculations, and updating globals for a single bill."""
    # Notify Python that we are modifying these global variables
    global total_bills, count_category_A, count_category_C
    global accum_total_pay, accum_high_bills

    print("\n--- 1. Bill Calculation ---")

    # 1. Input Data (using the 'reader' module)
    consumption_kwh = reader.read_positive_float("Enter Consumption (kWh): ")
    category = reader.read_category("Enter Category (A, B, C, D, E): ")
    exchange_rate = reader.read_positive_float("Enter Exchange Rate (Soles x USD): ")

    # 2. Get Rates (using the 'rates' module)
    # This function returns a tuple (base_rate, penalty_percentage)
    base_rate_usd, penalty_percentage = rates.get_data_by_category(category)

    # 3. Calculations
    amount_base_usd = consumption_kwh * base_rate_usd
    amount_base_soles = amount_base_usd * exchange_rate
    penalty_amount_soles = amount_base_soles * penalty_percentage

    total_pay_soles = amount_base_soles + penalty_amount_soles

    # 4. Update Globals
    total_bills += 1
    accum_total_pay += total_pay_soles

    if category == 'A':
        count_category_A += 1
    elif category == 'C':
        count_category_C += 1

    if total_pay_soles >= 600:
        accum_high_bills += total_pay_soles

    # 5. Individual Bill Report
    print("\n--- Bill Report ---")
    if consumption_kwh > 500:
        print("Message: Excessive consumption, risk of overload.")

    print(f"Base Amount in Soles: S/ {amount_base_soles:.2f}")
    print(f"Penalty Amount: S/ {penalty_amount_soles:.2f}")
    print(f"Total to Pay in Soles: S/ {total_pay_soles:.2f}")


def menu():
    """Displays the menu and handles navigation."""
    print("\n======== MAIN MENU ========")
    print("1. Calculate Bill")
    print("2. Report Counters and Accumulators")
    print("3. Exit")

    # Use the 'reader' module to get a valid option
    op = reader.read_menu_option("Enter an option: ", 1, 3)

    match op:
        case 1:
            process_bill()
        case 2:
            print_report()
        case 3:
            # Use the 'util' module for the exit message
            util.exit_system()

    return op


def executor():
    """Main program loop."""
    while True:
        option = menu()
        if option == 3:
            break


# --- Start the program ---
executor()