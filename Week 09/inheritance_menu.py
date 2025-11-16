# --- File: inheritance_menu.py ---
# This program calculates inheritance distribution using
# helper functions and a main menu loop.

def read_int():
    """Helper function to read an integer."""
    data = int(input(""))
    return data


def read_float():
    """Helper function to read a float."""
    data = float(input(""))
    return data


def calculate_inheritance():
    """Contains the main logic for the calculation."""
    # --- Validation loop for the inheritance amount ---
    while True:
        print("Enter Inheritance Amount: ")
        total_amount = read_float()

        if (total_amount <= 0):
            print("[ERROR] Re-enter, inheritance amount must be greater than 0")
        else:
            break

    # --- Validation loop for the number of children ---
    while True:
        print("Enter number of children: ")
        num_children = read_int()

        if (num_children <= 0):
            print("[ERROR] Re-enter, number of children must be greater than 0")
        else:
            break

    # --- Distribution Logic ---
    if (num_children <= 3):
        # Logic for 3 or fewer children: divide equally
        share = total_amount / num_children
        print(f"The share for each child is: {share}")

    elif (num_children >= 4):
        # Special logic for 4 or more children
        eldest_share = total_amount / 2
        # The other half is divided among the remaining children
        share = eldest_share / (num_children - 1)

        print(f"The share for the eldest child is: {eldest_share}")
        print(f"The share for the other children is: {share}")


def menu():
    """
    Main control function. This IS the main program loop.
    """
    # This outer loop keeps the menu repeating
    while True:
        print("\n========== MAIN MENU ==========\n")
        print("1. Process")
        print("2. Exit")

        # --- Nested validation loop for the menu option ---
        while True:
            menu_option = int(input("Enter a menu option: "))

            if (menu_option < 1 or menu_option > 2):
                print("[ERROR] Re-enter, invalid option")
            else:
                break

        match menu_option:
            case 1:
                # Calls the calculation logic
                calculate_inheritance()

            case 2:
                # --- Nested validation loop for exit confirmation ---
                while True:
                    confirm = input("Are you sure you want to exit? (Y/N): ")
                    confirm_upper = confirm.upper()

                    if (confirm_upper != "S" and confirm_upper != "N"):
                        print("[ERROR] Re-enter, invalid option")
                    else:
                        break

                if (confirm_upper == "S"):
                    print("Exiting the program...")
                    # This 'break' exits the main 'while True' loop, ending the program.
                    break


def executor():
    """A simple function to start the menu."""
    menu()


# --- This is the initial call that starts the entire program ---
executor()