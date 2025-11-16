# --- File: function_with_arguments.py ---
# This program finds the largest and smallest number from a series of inputs.
# It demonstrates passing arguments to a function and using global variables.

global counter
counter = 0

# These global variables will store the largest (may) and smallest (men) values
global may
global men

def find_max_min(data_entered, counter):
    """
    Receives the new data and the current count,
    then updates the global 'may' and 'men' variables.
    """
    global may
    global men

    if (counter == 1):
        # On the first run, initialize 'may' and 'men' to the first value
        may = data_entered
        men = data_entered
    elif (data_entered > may):
        # If the new data is larger, update 'may'
        may = data_entered
    else:
        # If it's not larger, check if it's smaller
        if (data_entered < men):
            men = data_entered

def executor():
    """Main function to run the input loop."""
    global counter

    while True:
        print(50 * "=")

        data_entered = eval(input("Enter a value: "))
        counter = counter + 1

        # --- Argument Passing ---
        # The values of 'data_entered' and 'counter' are passed
        # as arguments to the find_max_min function.
        find_max_min(data_entered, counter)

        # --- Input Validation Loop ---
        while True:
            response = input("Do you want to enter another value? (Y/N): ")
            response_upper = response.upper()

            if (response_upper != "Y" and response_upper != "N"):
                print("[ERROR] Invalid option, re-enter")
            else:
                break # Exit the validation loop

        if (response_upper != "Y"):
            # If the user enters 'N', print the final report and break the main loop
            print(f"The largest value is: {may}")
            print(f"The smallest value is: {men}")
            break

# --- Start the program ---
executor()