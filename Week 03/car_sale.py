from datetime import datetime # Import the datetime library for dates

############# START OF DATA ENTRY #############
print("\n========== DATA ENTRY ==========\n") # Program Title

print("********* CLIENT *********") # Client data
clientID = int(input("Enter client ID (DNI): "))
lastName = input("Enter client last name: ")
firstName = input("Enter client first name: ")
clientFullName = firstName + " " + lastName # Concatenate name

print("\n********* VEHICLE *********") # Vehicle data
brand = input("Enter vehicle brand: ")
model = input("Enter vehicle model: ")
year = int(input("Enter vehicle year: "))
priceUSD = float(input("Enter vehicle price in USD: "))

print("********* EXCHANGE RATE *********") # Exchange rate
exchangeRate = float(input("Enter the exchange rate to Soles: "))
############# END OF DATA ENTRY #############

############# START OF PROCESSES #############
# Calculating
TAX_RATE = 0.19 # 19% tax
taxUSD = priceUSD * TAX_RATE
totalUSD = priceUSD + taxUSD

# Corrected calculation for tax in Soles
taxSoles = taxUSD * exchangeRate
totalSoles = totalUSD * exchangeRate

# Generating the payment receipt
receiptNumber = input("Enter the receipt number: ")
now = datetime.now() # Current date
currentYear = now.year # Current year
currentMonth = now.month # Current month
currentDay = now.day # Current day
############## END OF PROCESSES #############

############# DATA OUTPUT #############
print("\n========== DATA REPORT ==========\n") # Report Title
print("********* PAYMENT RECEIPT *********") # Receipt Title
print(f"Receipt Number: {receiptNumber}")
print(f"Client ID: {clientID}")
print(f"Client: {clientFullName}")
print(f"Issue Date: {currentDay}/{currentMonth}/{currentYear}")
print(f"Amount to pay in USD: $ {totalUSD:.2f}")
print(f"Tax in USD (19%): $ {taxUSD:.2f}")
print(f"Amount to pay in Soles: S/. {totalSoles:.2f}")
print(f"Tax in Soles (19%): S/. {taxSoles:.2f}")
print("\nCongratulations on your purchase...!")

print("\n========== END OF PROGRAM ==========\n") # End of program