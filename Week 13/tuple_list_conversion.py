print("===== SCHEDULE DATA =====")


def enter_tuple_data():
    """
    Demonstrates creating a tuple by filling a list first.
    """
    schedule_tuple = ()  # Create an empty tuple

    # Convert tuple to list to be able to use .append()
    schedule_list = list(schedule_tuple)

    for i in range(3):
        value = input("Enter value: ")
        schedule_list.append(value)

    # Convert back to tuple to make it immutable again
    schedule_tuple = tuple(schedule_list)
    return schedule_tuple


def display_tuple_data(my_tuple):
    if my_tuple:
        print("The elements of the tuple are:")
        for element in my_tuple:
            print(element, ", ", end="")
        print()  # New line at the end
    else:
        print("The tuple is empty or contains invalid elements.")


# --- Main Execution ---
my_tuple = enter_tuple_data()
display_tuple_data(my_tuple)