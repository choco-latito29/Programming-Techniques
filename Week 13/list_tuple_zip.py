# --- File: list_tuple_zip.py ---
# This program demonstrates how to work with Lists (mutable) and Tuples (immutable),
# and how to combine them using the zip() function.

# Global variables
global my_list
global my_tuple

my_list = []
my_tuple = ()

def register_tuple():
    """
    Registers a tuple of products.
    Tuples are defined with parentheses () and cannot be changed (Immutable).
    """
    global my_tuple
    my_tuple = ('Paper', 'Notebook', 'Pen', 'Pencil')
    print("-> Product tuple registered.")

def register_list():
    """
    Registers a list of prices.
    Lists are defined with brackets [] and can be modified (Mutable).
    """
    global my_list
    # We define 4 prices corresponding to the 4 products
    my_list = [5.00, 8.50, 3.00, 2.50]
    print("-> Price list registered.")

def show_product_prices():
    """Combines the tuple and list to display a report."""
    print("\n--- Showing Products and Prices ---")

    # Ensure data is populated
    register_list()
    register_tuple()

    # The zip() function takes two iterables (tuple and list) and pairs them up.
    # It creates a list of tuples: [('Paper', 5.0), ('Notebook', 8.5), ...]
    report = list(zip(my_tuple, my_list))

    print("\nReport (Product, Price):")
    # Iterate through the combined pairs
    for product, price in report:
        print(f"- Product: {product}, Price: S/ {price:.2f}")

def menu():
    """Displays the menu and validates user input."""
    print("\n======== WEEK 13 MENU ========")
    print("1. Show Product/Price Report")
    print("2. Exit")

    while True:
        try:
            op = int(input("Enter an option: "))
            if (op < 1 or op > 2):
                print("[ERROR] Invalid option. Enter 1 or 2.")
            else:
                return op
        except ValueError:
            print("[ERROR] Please enter a number.")

def run():
    """Main program loop."""
    while True:
        option = menu()
        if option == 1:
            show_product_prices()
        elif option == 2:
            print("Exiting program...")
            break

# --- Start the program ---
run()