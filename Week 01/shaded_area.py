# Folder: Week 01 Programs
# Program Name: ProposedProgram2Piece

# This program calculates the shaded area of a mechanical part based on the side of a square.
# The area is the area of the square minus the area of a circle.
import math

print("==== Template Area Calculation ====")

# Request the side length of the square
square_side = float(input("Enter the side length of the square: "))

# The area of the square is side * side
square_area = square_side * square_side

# The circle's diameter is equal to the square's side, so the radius is side / 2
radius = square_side / 2

# The area of the circle is pi * radius^2
circle_area = math.pi * (radius ** 2)

# The shaded area is the area of the square minus the area of the circle
shaded_area = square_area - circle_area

# Print the result
print(f"The shaded area of the template is: {shaded_area}")