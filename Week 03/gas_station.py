print("\n========== DATA ENTRY ==========\n") # Program Title

CONVERSION_RATE = 4 # Liters per gallon

gallonsPurchased = int(input("Enter the number of gallons: ")) # Amount of gallons purchased
pricePerLiter = float(input("Enter the price of gasoline per liter: ")) # Price per liter

litersDispensed = gallonsPurchased * CONVERSION_RATE # Convert gallons to liters
totalCost = litersDispensed * pricePerLiter # Calculate the total cost

print("\n========== PAYMENT REPORT ==========\n") # Report Title
print(f"Gallons dispensed: {gallonsPurchased}") # Show the amount of gallons dispensed
print(f"Price per liter: S/. {pricePerLiter:.2f}") # Show the price per liter
print(f"Total to pay: S/. {totalCost:.2f}") # Show the total to pay

print("\n========== END OF PROGRAM ==========\n") # End of program