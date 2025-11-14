print("\n========== MENU ==========\n") # Program Title

print("1. Wantan Soup\n2. Fried Rice\n3. Drink\n4. Dessert\n") # Restaurant Menu

print("\n========== DATA ENTRY ==========\n") # Data Entry Title
priceSoup = float(input("Enter the price for Wantan Soup: S/. ")) # Price of Wantan Soup
qtySoup = int(input("Enter the quantity for Wantan Soup: ")) # Quantity of Wantan Soup

priceRice = float(input("Enter the price for Fried Rice: S/. ")) # Price of Fried Rice
qtyRice = int(input("Enter the quantity for Fried Rice: ")) # Quantity of Fried Rice

priceDrink = float(input("Enter the price for Drink: S/. ")) # Price of Drink
qtyDrink = int(input("Enter the quantity for Drink: ")) # Quantity of Drink

priceDessert = float(input("Enter the price for Dessert: S/. ")) # Price of Dessert
qtyDessert = int(input("Enter the quantity for Dessert: ")) # Quantity of Dessert

subTotalSoup = priceSoup * qtySoup # Subtotal for Wantan Soup
subTotalRice = priceRice * qtyRice # Subtotal for Fried Rice
subTotalDrink = priceDrink * qtyDrink # Subtotal for Drink
subTotalDessert = priceDessert * qtyDessert # Subtotal for Dessert

amountToPay = subTotalSoup + subTotalRice + subTotalDrink + subTotalDessert # Total amount to pay

print("\n========== INVOICE ==========\n") # Invoice Title
print(f"The subtotal for Wantan Soup is: S/. {subTotalSoup:.2f}") # Show subtotal for Wantan Soup
print(f"The subtotal for Fried Rice is: S/. {subTotalRice:.2f}") # Show subtotal for Fried Rice
print(f"The subtotal for Drink is: S/. {subTotalDrink:.2f}") # Show subtotal for Drink
print(f"The subtotal for Dessert is: S/. {subTotalDessert:.2f}") # Show subtotal for Dessert
print(f"The total amount to pay is: S/. {amountToPay:.2f}") # Show the total amount to pay

print("\n========== END OF PROGRAM ==========\n") # End of program