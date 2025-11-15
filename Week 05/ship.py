print("\n========== SHIP DATA ENTRY ==========")

# Ask the user for a single letter representing a ship type
letter = input("Enter a ship's code letter (B, F, C): ")
upperLetter = letter.upper()  # Convert to uppercase for matching

# First, check if the letter is one of the valid options
if upperLetter == "B" or upperLetter == "F" or upperLetter == "C":

    # Use match-case to find the specific ship type
    match upperLetter:
        case "B":
            print("It's a Battleship.")
        case "F":
            print("It's a Frigate.")
        case "C":
            print("It's a Cruiser.")
else:
    # This runs if the 'if' statement was False
    print("ERROR: That is not a valid ship letter.")