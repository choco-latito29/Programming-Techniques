print("\n========== DATA ENTRY ==========\n") # Print the program title

menCount = int(input("Enter the number of men: ")) # Enter the number of men
womenCount = int(input("Enter the number of women: ")) # Enter the number of women

totalStudents = menCount + womenCount # Calculate the total number of students

menPercentage = round((menCount * 100) / totalStudents) # Calculate the percentage of men
womenPercentage = round((womenCount * 100) / totalStudents) # Calculate the percentage of women

print("\n========== REPORT ==========") # Print the report title
print(f"The percentage of Men is: {menPercentage}%") # Show the percentage of men
print(f"The percentage of Women is: {womenPercentage}%") # Show the percentage of women