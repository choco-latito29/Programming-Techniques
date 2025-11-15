"""
We will enter 4 grades.
Enter an extra grade.
Replace the extra grade with the lowest grade.
Display the lowest grade.
Display the previous average.
Display the new average.
"""

print("\n========== STUDENT GRADE CALCULATION ==========\n")

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
grade4 = float(input("Enter the fourth grade: "))

initial_average = (grade1 + grade2 + grade3 + grade4) / 4
print(f"The initial average is: {initial_average:.2f}")

# min() is a built-in function that finds the smallest value
low_grade = min(grade1, grade2, grade3, grade4)
print(f"The lowest grade is: {low_grade}")

# Get user consent and convert to uppercase for easy comparison
option = input("Do you want to enter an additional task grade to replace the lowest grade? (YES/NO): ").upper()

if option == "YES":

    extra_grade = float(input("Enter the additional task grade: "))

    # This if/elif chain finds the first variable that matches
    # the low_grade and replaces its value.
    if grade1 == low_grade:
        grade1 = extra_grade
    elif grade2 == low_grade:
        grade2 = extra_grade
    elif grade3 == low_grade:
        grade3 = extra_grade
    elif grade4 == low_grade:
        grade4 = extra_grade

    new_average = (grade1 + grade2 + grade3 + grade4) / 4

    print(f"\nReplaced grade {low_grade} with {extra_grade}.")
    print(f"The new grades are: {grade1}, {grade2}, {grade3}, {grade4}")
    print(f"The new average is: {new_average:.2f}")

else:
    print("\nNo modifications were made to the grades.")

print("\n--- End of Program ---")