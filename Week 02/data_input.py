# Enter product name, price, quantity, and a discount
# Calculate the payment amount

print("\n========== DATA ENTRY ==========\n")

productName = input("Enter the product name: ") # Enter the product name

productPrice = float(input("Enter the product price: ")) # Enter the product price

productQuantity = int(input("Enter the product quantity: ")) # Enter the product quantity

discountPercentage = float(input("Enter the discount percentage: ")) # Enter the discount percentage

grossAmount = productPrice * productQuantity # Calculate the gross amount
discountAmount = grossAmount * (discountPercentage / 100) # Calculate the discount amount
paymentAmount = grossAmount - discountAmount # Calculate the amount to pay

print("\n========== REPORT ==========\n") # Print the report title
print(f"The Gross Amount is: {grossAmount}") # Show the Gross Amount
print(f"The Discount Amount is: {discountAmount}") # Show the Discount Amount
print(f"The Amount to Pay is: {paymentAmount}") # Show the Amount to Pay