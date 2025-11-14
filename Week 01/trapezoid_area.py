# This program calculates the area of a piece of land shaped like a right trapezoid.

print("==== Land Area Calculation (Trapezoid) ====")

# Request lengths A and B from the user
length_A = float(input("Enter length A (base 1): "))
length_B = float(input("Enter length B (base 2 and height): "))

# Calculate the area of the trapezoid
# The bases are A and B, and the height is B.
trapezoid_area = ((length_A + length_B) / 2) * length_B

# Print the result
print(f"The total area of the land is: {trapezoid_area}")