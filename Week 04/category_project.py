print("\n========== DATA ENTRY ==========\n")

baseAmountUSD = float(input("Enter the base amount in dollars: "))

print("\nCategory\n\n1. Category V\n2. Category R\n3. Category P\n4. Category A\n5. Category L\n")
category = input("Enter the category: ") # User inputs a string, e.g., "1"

print("\nProject Type\n\n1. Housing\n2. Recreational\n3. Pool\n4. Auditorium\n5. Building\n")
project = input("Enter the project type: ") # User inputs a string, e.g., "1"

discount = 0

# --- Logical Error 1: Comparing a string (from input) to an integer ---
if category == 1 and project == 1: # This will always be False
    discount = 5
elif category == 2 and project == 2: # This will always be False
    discount = 10
elif category == 3 and project == 2:
    discount = 15
elif category == 4 and project == 2:
    discount = 20
elif category == 5 and project == 5:
    discount = 25
else:
    discount = 0 # This 'else' block will always run

exchangeRate = float(input("\nEnter the exchange rate: "))

# --- Logical Error 2: Currency conversion is inverted ---
montoBaseSoles = baseAmountUSD / exchangeRate
montoDescuento = (montoBaseSoles * discount) / 100
montoPagar = montoBaseSoles - montoDescuento

print("\n========== RESULTS ==========\n")
print(f"The Base Amount in Soles is: {montoBaseSoles:.2f}")

# --- Logical Error 3: Printing the discount amount, not the final price ---
print(f"The amount with discount is: {montoDescuento:.2f}")

print("\nEnd of Program\n")