# --- File: lottery_sets.py ---
# This program demonstrates operations with Python Sets:
# Union, Intersection, Difference, and Symmetric Difference.

def process_set_data():
    """
    Creates two sets based on user input and performs set operations.
    """
    # 1. Create empty sets
    lottery_numbers = set()
    attempts_set = set()

    print("\n--- Enter Lottery Numbers ---")
    for i in range(5):
        num = input(f"Enter lottery number {i+1}: ")
        # .add() inserts an element into the set
        lottery_numbers.add(num)

    print("\n--- Enter Attempt Numbers ---")
    for i in range(3):
        attempt = input(f"Enter attempt number {i+1}: ")
        attempts_set.add(attempt)

    # 2. Display Original Sets
    print("\n----- LOTTERY NUMBERS SET: -----")
    print(lottery_numbers)

    print("\n----- ATTEMPTS SET: -----")
    print(attempts_set)

    # 3. Set Operations
    print("\n----- UNION (|) -----")
    # Union: All unique elements from both sets
    set_union = lottery_numbers | attempts_set
    print(set_union)

    print("\n----- INTERSECTION (&) -----")
    # Intersection: Only elements present in BOTH sets
    set_intersection = lottery_numbers & attempts_set
    print(set_intersection)

    print("\n----- DIFFERENCE (-) -----")
    # Difference: Elements in Lottery that are NOT in Attempts
    set_difference = lottery_numbers - attempts_set
    print(set_difference)

    print("\n----- SYMMETRIC DIFFERENCE (^) -----")
    # Symmetric Diff: Elements in either set, but NOT in both
    set_sym_difference = lottery_numbers ^ attempts_set
    print(set_sym_difference)


def menu():
    """Displays the menu and handles navigation."""
    print("\n======== SETS MAIN MENU ========")
    print("1. Process Sets")
    print("2. Exit")

    while True:
        try:
            op = int(input("Enter an option: "))
            if op < 1 or op > 2:
                print("ERROR. Please re-enter.")
            else:
                break
        except ValueError:
            print("ERROR. Please enter a number.")

    match op:
        case 1:
            process_set_data()

        case 2:
            while True:
                response = input("Do you want to exit? (Y/N): ").upper()
                if response != 'Y' and response != 'N':
                    print("ERROR. Please re-enter Y or N.")
                else:
                    break

            if response == 'Y':
                print("Exiting...")
            else:
                # Recursive call to show menu again if not exiting
                menu()

    return op


def run_app():
    """Main execution loop."""
    while True:
        option = menu()
        # Break the loop if user chose option 2 (Exit)
        if option == 2:
            break

# --- Start the program ---
run_app()