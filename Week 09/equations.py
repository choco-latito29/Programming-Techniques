print("=" * 50)

def read_integer():
    """Reads an integer value from the user."""
    data = int(input(""))
    return data

def calculate_y():
    """Asks for X and calculates Y based on conditional logic."""
    print("Enter the value of X: ")
    x = read_integer()

    # Chained conditional (if-elif) to determine the value of 'y'
    if (x <= 0):
        y = (x ** 2) + 5
    elif (x > 0 and x < 2):
        y = (3 * x) - 1
    elif (x >= 2):
        y = (x ** 2) - (4 * x) + 5

    print(f"The value of Y is: {y}")

def executor():
    """Main function to run the program."""
    calculate_y()

# --- Start the program ---
executor()