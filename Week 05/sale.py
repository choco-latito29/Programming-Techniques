print("\n ========== DATA ENTRY ==========\n")

productName = input("Enter the product name: ")
productPrice = float(input("Enter the product price: "))

# 1. Price validation
if (productPrice > 0):
    productQty = int(input("Enter product quantity: "))

    # 2. Quantity validation (nested)
    if (productQty > 0):
        discountPercentage = float(input("Enter the discount percentage: "))

        # 3. Discount validation (nested)
        if (discountPercentage > 0):
            gender = (input("Enter the gender (M/F): "))
            genderUpper = gender.upper()

            # 4. Gender validation (nested)
            if (genderUpper == "F" or genderUpper == "M"):

                match genderUpper:
                    case "M":
                        bonus = 0.18
                        if (productQty <= 10):
                            discount_rate = 0.2
                        else:
                            discount_rate = 0.5
                    case "F":
                        bonus = 0.25
                        if (productQty <= 10):
                            discount_rate = 0.3
                        else:
                            discount_rate = 0.4

                # Note: The 'discount_rate' variable (0.2, 0.5, etc.) is calculated but never used.

                # Calculations use the user-inputted 'discountPercentage'
                grossAmount = productPrice * productQty
                bonusAmount = grossAmount * bonus
                discountAmount = (grossAmount * discountPercentage) / 100
                paymentAmount = grossAmount - discountAmount + bonusAmount

                print("\n========== REPORT ==========\n")
                print(f"The gross amount is: {grossAmount}")
                print(f"The bonus amount is: {bonusAmount}")
                print(f"The discount amount is: {discountAmount}")
                print("---------------------------------------")
                print(f"The amount to pay is: {paymentAmount}")

            else:
                print("Gender error")
        else:
            print("Percentage error")
    else:
        print("Quantity error")
else:
    print("Price error")