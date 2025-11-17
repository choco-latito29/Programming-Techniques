print("===== SCHEDULE DATA =====")


def enter_tuple_data():
    """
    Demonstrates how to 'add' to a tuple by creating a new one.
    """
    schedule_tuple = ()  # Create an empty tuple

    for i in range(3):
        value = input("Enter value: ")

        # Concatenate the existing tuple with a new single-item tuple
        # Note the comma after 'value' to make it a tuple
        schedule_tuple = schedule_tuple + (value,)

    return schedule_tuple  # Return the complete tuple


print(enter_tuple_data())