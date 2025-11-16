# --- File: hanoi.py ---
# This program solves the Towers of Hanoi puzzle
# using recursion and counts the total moves.

print("=" * 50)


def hanoi(n, org, aux, des):
    """
    Solves the puzzle for 'n' disks, moving from 'org' (origin)
    to 'des' (destination) using 'aux' (auxiliary).
    Returns the number of moves made.
    """
    moves = 0

    # 1. Base Case: The simplest step
    if (n == 1):
        # If there's only one disk, move it directly
        print(org, " -> ", des)
        moves = 1

    # 2. Recursive Step: For more than one disk
    else:
        # Step A: Move (n-1) disks from Origin to Auxiliary
        moves += hanoi(n - 1, org, des, aux)

        # Step B: Move the 1 largest disk from Origin to Destination
        print(org, " -> ", des)
        moves += 1

        # Step C: Move the (n-1) disks from Auxiliary to Destination
        moves += hanoi(n - 1, aux, org, des)

    # 3. Return the total moves for this step
    return moves


def executor():
    """Main function to get user input and start the puzzle."""

    # --- Validation Loop ---
    while True:
        n = int(input("Enter the number of disks: "))

        if (n <= 0):
            print("[ERROR] Please re-enter...")
        else:
            break

    print("\nStarting moves:\n")

    # --- Start the puzzle ---
    # Call the hanoi function and capture the total moves returned
    total_moves = hanoi(n, "A", "B", "C")

    print("\n--- Process Complete ---")
    print(f"Total moves made: {total_moves}")


# --- Start the program ---
executor()