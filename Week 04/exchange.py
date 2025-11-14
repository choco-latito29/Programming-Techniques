print("\n========== DATA ENTRY ==========\n") # Program Title

solesAmount = float(input("Enter the amount in soles: ")) # Amount in soles to convert

usdExchangeRate = float(input("Enter the USD exchange rate (e.g., 3.80): ")) # USD exchange rate
eurExchangeRate = float(input("Enter the EUR exchange rate (e.g., 4.10): ")) # EUR exchange rate

# Logical Error: This is converting FROM USD/EUR TO Soles
solesToDollars = solesAmount * usdExchangeRate
solesToEuros = solesAmount * eurExchangeRate

print("\n========== REPORT (Incorrect Logic) ==========\n") # Report Title
print(f"The amount in dollars is: {solesToDollars:.2f} $")
print(f"The amount in euros is: {solesToEuros:.2f} €")