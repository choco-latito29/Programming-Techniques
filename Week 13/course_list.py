print("======= Course Data =======")

course_list = []

# Ask the user how many items they want to add
max_range = int(input("Enter the maximum range: "))

def enter_list_data():
    """
    Asks the user for input 'max_range' times
    and appends the values to the list.
    """
    for i in range(max_range):
        value = input("Enter the value: ")
        course_list.append(value)

def show_list_data(current_list):
    """
    Checks if the list is not empty and prints its contents.
    """
    if current_list:
        print("The elements of the list are: ")
        for element in current_list:
            print(element, " ", end=" ")
        print() # Add a newline at the end
    else:
        print("The list is empty or contains invalid elements")

# --- Start the program ---
enter_list_data()
show_list_data(course_list)