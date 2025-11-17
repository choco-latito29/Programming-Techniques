# --- File: tuple_operations.py ---
# This program demonstrates basic operations with Tuples.
# Remember: Tuples are IMMUTABLE (cannot be changed directly).

print("===== TUPLE OPERATIONS =====")

# 1. Creating a Tuple
# We define some variables first
days_count = 5
start_time = "8:00 AM"
end_time = "1:00 PM"

# Create the tuple packing these values
schedule = (days_count, start_time, end_time)

# 2. ITERATING through the Tuple
# We use range(len()) to get indices 0, 1, 2
print("\n--- Iteration ---")
for i in range(len(schedule)):
    # We access elements using brackets [], just like a list
    print(f"Element at index {i}: {schedule[i]}")

# ------------------------------------------------------- #

# 3. "MODIFYING" a Tuple (Concatenation)
print("\n--- Adding an element ---")
# Since tuples are immutable, we cannot use .append().
# Instead, we create a NEW tuple by adding another tuple to it.

# Important: A single-element tuple needs a comma, e.g., ("Lunch",)
new_element = ("Lunch Break",)
schedule = schedule + new_element

print(f"New Tuple: {schedule}")

# ------------------------------------------------------- #

# 4. Converting Tuple to List
print("\n--- Converting to List ---")
# If we really need to edit elements, we convert to a list first
schedule_list = list(schedule)
schedule_list[0] = 6 # Now we can change the days count
print(f"Modified List: {schedule_list}")