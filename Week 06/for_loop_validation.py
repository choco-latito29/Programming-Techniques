print("\n========== DATA ENTRY ==========\n")

totalPrice = 0

# The 'for' loop will run 10 times (i = 0, 1, 2... 9)
for i in range (10):
    # This 'while True' loop is nested inside the 'for' loop
    # It will repeat until the user enters a valid price
    while True:
        productPrice = float(input(f"Enter price for product {i + 1}: "))

        if (productPrice <= 0):
            print("[ERROR] please re-enter")
        else:
            break # Exits the 'while' loop

    # This line runs after the 'while' loop breaks
    totalPrice = totalPrice + productPrice

# After the 'for' loop finishes, the discount is calculated
if totalPrice > 200:
    discountRate = 0.15
else:
    discountRate = 0

discountAmount = totalPrice * discountRate
# --- Logical Error 1: Should subtract 'discountAmount' ---
paymentAmount = totalPrice - discountRate

print("\n========== REPORT ==========\n")
# --- Logical Error 2: This line prints the subtotal ---
print(f"The amount to pay is: {totalPrice}")
print(f"The discount amount is: {discountAmount}")
print(f"The amount to pay is: {paymentAmount}")