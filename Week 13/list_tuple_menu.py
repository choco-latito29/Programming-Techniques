# --- File: list_tuple_menu.py ---
# This program combines List and Tuple operations in a single menu-driven application.
# It allows the user to define the size of the data structures dynamically.

def enter_list_data():
    """
    Asks the user for the size of the list and populates it.
    Returns the created list.
    """
    course_list = []

    # Dynamic range: User decides how many elements to add
    size = int(input("Enter the size of the list: "))

    for i in range(size):
        value = input(f"Enter value {i + 1}/{size}: ")
        course_list.append(value)

    print("List created successfully!")
    return course_list


def display_list_data(my_list):
    """Displays the elements of the list."""
    if my_list:
        print("\n--- Showing List ---")
        print("The elements of the list are: ")
        for element in my_list:
            print(element, ", ", end="")
        print()  # New line
    else:
        print("\n[WARNING] The list is empty. Use option 1 to enter data.")


def enter_tuple_data():
    """
    Asks the user for data, creates a temporary list,
    and converts it to a Tuple (since tuples are immutable).
    """
    temp_list = []

    size = int(input("Enter the size of the tuple: "))

    for i in range(size):
        value = input(f"Enter value {i + 1}/{size}: ")
        temp_list.append(value)

    # Convert the list to a tuple before returning
    schedule_tuple = tuple(temp_list)

    print("Tuple created successfully!")
    return schedule_tuple


def display_tuple_data(my_tuple):
    """Displays the elements of the tuple."""
    if my_tuple:
        print("\n--- Showing Tuple ---")
        print("The elements of the tuple are:")
        for element in my_tuple:
            print(element, ", ", end="")
        print()  # New line
    else:
        print("\n[WARNING] The tuple is empty. Use option 3 to enter data.")


def menu():
    """Displays the menu and validates the option."""
    print("\n======== LISTS AND TUPLES MENU ========")
    print("1. Enter List Data")
    print("2. Show List Data")
    print("3. Enter Tuple Data")
    print("4. Show Tuple Data")
    print("5. Exit")

    while True:
        try:
            op = int(input("Enter an option: "))
            if (op < 1 or op > 5):
                print("[ERROR] Invalid option. Enter between 1 and 5.")
            else:
                return op
        except ValueError:
            print("[ERROR] Please enter a number.")


def run_app():
    """Main execution loop."""
    # Variables to store data in memory during execution
    main_list = []
    main_tuple = ()

    while True:
        option = menu()

        match option:
            case 1:
                main_list = enter_list_data()
            case 2:
                display_list_data(main_list)
            case 3:
                main_tuple = enter_tuple_data()
            case 4:
                display_tuple_data(main_tuple)
            case 5:
                print("Exiting the program...")
                break


# --- Start the program ---
run_app()