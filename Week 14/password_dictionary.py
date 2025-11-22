# --- File: password_dictionary.py ---
# This program demonstrates how to use a Dictionary to store
# key-value pairs (Username: Password).

print("===== USER DATA: PASSWORD =====")

# Initialize an empty dictionary
password_dictionary = {}


def enter_dictionary_data():
    """
    Asks the user for 3 username/password pairs
    and stores them in the dictionary.
    """
    for i in range(3):
        print(f"========= USER: {i + 1} =========")
        key = input("Enter username: ")
        value = input("Enter password: ")

        # Syntax to add/update a dictionary item: dict[key] = value
        password_dictionary[key] = value


def show_dictionary_data():
    """Displays the contents of the dictionary."""
    # Check if dictionary is not empty
    if password_dictionary:
        print("The elements of the dictionary are: ")
        # .items() returns a view of (key, value) pairs
        for key, value in password_dictionary.items():
            print(f"{key}: {value}", " ", end="")
        print()  # New line
    else:
        print("The dictionary is empty.")


def menu():
    """Displays the menu and handles navigation."""
    print("\n======== MAIN MENU ========")
    print("1. Enter Users and Passwords")
    print("2. Show Dictionary")
    print("3. Exit")

    while True:
        try:
            op = int(input("Enter an option: "))
            if op < 1 or op > 3:
                print("ERROR. Please re-enter.")
            else:
                break
        except ValueError:
            print("ERROR. Please enter a number.")

    match op:
        case 1:
            enter_dictionary_data()
        case 2:
            show_dictionary_data()
        case 3:
            while True:
                response = input("Do you want to exit? (Y/N): ").upper()
                if response != 'Y' and response != 'N':
                    print("ERROR. Please re-enter Y or N.")
                else:
                    break

            if response == 'Y':
                print("Exiting...")
            else:
                menu()  # Go back to menu if not exiting

    return op


def run_app():
    """Main execution loop."""
    while True:
        option = menu()
        if option == 3:
            break


# --- Start the program ---
run_app()