print("===== FINAL GRADE CALCULATION =====") # Show the program title

c1 = float(input("Enter the grade for C1: ")) # Grade for consolidated 1
ep = float(input("Enter the grade for Midterm Exam: ")) # Grade for midterm exam
c2 = float(input("Enter the grade for C2: ")) # Grade for consolidated 2
ef = float(input("Enter the grade for Final Exam: ")) # Grade for final exam

# Calculate the final grade based on weighted percentages
final_grade = (c1 * 0.20) + (ep * 0.25) + (c2 * 0.20) + (ef * 0.35)

print(f"The final grade is: {final_grade:.2f}") # Show the final grade with two decimals