print("\n========== DATA ENTRY ==========\n") # Program Title

COMMISSION_PERCENTAGE = 0.08 # Commission percentage (8%)

baseSalary = float(input("Enter the base salary: S/. ")) # Base salary
salesAmount = float(input("Enter sales amount: S/. ")) # Sales amount

commissionAmount = salesAmount * COMMISSION_PERCENTAGE # Calculate the commission amount
netSalary = baseSalary + commissionAmount # Calculate the net salary

print("\n========== DATA REPORT ==========\n") # Report Title
print(f"Commission Percentage: {COMMISSION_PERCENTAGE * 100}%") # Show the commission percentage
print(f"The commission amount is: S/. {commissionAmount:.2f}") # Show the commission amount
print(f"The net salary is: S/. {netSalary:.2f}") # Show the net salary

print("\n========== END OF PROGRAM ==========\n") # End of program