# --- File: client_invoices.py ---
# This program demonstrates how to work with Dictionaries and Sets together.
# It simulates mapping clients (Dictionary) to invoices (Set).

# Global variables
global my_dictionary
global my_set

my_dictionary = {}
my_set = set()


def register_dictionary():
    """Populates the dictionary with client data."""
    global my_dictionary
    # Dictionary: key = clientID, value = name
    my_dictionary = {
        'client1': 'Juan Lopez',
        'client2': 'Ana Sanchez',
        'client3': 'Carlos Diaz'
    }
    print("-> Dictionary registered.")


def register_set():
    """Populates the set with invoice IDs."""
    global my_set
    # Sets are unordered collections of unique elements
    my_set = {'invoice1', 'invoice2', 'invoice3', 'invoice4', 'invoice5', 'invoice6', 'invoice7'}
    print("-> Set registered.")


def show_dictionary():
    """Displays the current dictionary content."""
    print("\n--- DICTIONARY CONTENT ---")
    print(my_dictionary)


def show_set():
    """Displays the current set content."""
    print("\n--- SET CONTENT ---")
    print(my_set)


def show_client_invoice_report():
    """
    Combines the dictionary keys and set elements into a tuple.
    """
    # Ensure data exists
    register_dictionary()
    register_set()

    # zip() stops at the shortest iterable. 
    # Dictionary (3 items) vs Set (7 items) -> Result will have 3 items.
    # Note: Since sets are unordered, the pairing might vary.
    report = tuple(zip(my_dictionary, my_set))

    print("\n--- REPORT: CLIENT - INVOICE ---")
    print(report)


def menu():
    """Displays the menu and handles user input."""
    print("\n======== MAIN MENU ========")
    print("1. Register and Report (Client - Invoice)")
    print("2. Show Dictionary")
    print("3. Show Set")
    print("4. Exit")

    while True:
        try:
            op = int(input("Enter an option: "))
            if op < 1 or op > 4:
                print("ERROR. Please re-enter 1-4.")
            else:
                break
        except ValueError:
            print("ERROR. Please enter a number.")

    match op:
        case 1:
            show_client_invoice_report()
        case 2:
            show_dictionary()
        case 3:
            show_set()
        case 4:
            while True:
                response = input("Do you want to exit? (Y/N): ").upper()
                if response != 'Y' and response != 'N':
                    print("ERROR. Please re-enter Y or N.")
                else:
                    break

            if response == 'Y':
                print("Exiting...")
            else:
                # Recursive call to return to menu
                menu()

    return op


def run_app():
    """Main execution loop."""
    while True:
        option = menu()
        if option == 4:
            break


# --- Start the program ---
run_app()