print("\n========== RESTAURANT BILL CALCULATION ==========\n")

consumption = float(input("Enter the consumption amount (S/.): "))

# 1. Validate that consumption is a positive number
if (consumption > 0):

    # 2. Determine the discount percentage
    if consumption <= 30:
        discount_rate = 0.10  # 10% discount
    else:
        discount_rate = 0.20  # 20% discount

    # 3. Calculate all values
    discount_amount = consumption * discount_rate
    subtotal = consumption - discount_amount
    tax = subtotal * 0.18  # 18% tax
    total_to_pay = subtotal + tax

    # 4. Print the detailed receipt
    print("\n========== DETAILED RECEIPT ==========\n")
    print(f"Consumption:      S/. {consumption:.2f}")
    print(f"Discount:         S/. {discount_amount:.2f}")
    print(f"Subtotal:         S/. {subtotal:.2f}")
    print(f"Tax (18%):        S/. {tax:.2f}")
    print("---------------------------------------")
    print(f"AMOUNT TO PAY:    S/. {total_to_pay:10.2f}")

else:
    # This 'else' catches non-positive numbers from the first 'if'
    print("[ERROR] The consumption amount must be greater than zero.")