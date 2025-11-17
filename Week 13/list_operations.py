print("===== LIST OPERATIONS =====")

# 1. Creating a list
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# 2. ITERATING through the list
# Using range(len()) to get indices 0, 1, 2, 3, 4
print("\n--- Iteration ---")
for i in range(len(days)):
    print(f"Day at index {i} is: {days[i]}")

# ------------------------------------------------------- #

# 3. CONCATENATING Lists (Joining)
print("\n--- Concatenation ---")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
shifts = [1, 2]

# The '+' operator joins two lists into a new one
schedule = days + shifts
print(f"Concatenated list: {schedule}")

# ------------------------------------------------------- #

# 4. LIST SLICING (Rebanado)
# Slicing creates a NEW list from a subset of the original.
print("\n--- Slicing ---")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Slice from index 1 up to (but not including) index 3
# Returns: ['Tuesday', 'Wednesday']
print(f"Slice [1:3] (from index 1 to <3): {days[1:3]}")

# ------------------------------------------------------- #

# Slice from the beginning (0) up to (but not including) index 3
# Returns: ['Monday', 'Tuesday', 'Wednesday']
print(f"Slice [:3] (from start to <3): {days[:3]}")

# ------------------------------------------------------- #

# Slice from index 3 to the end
# Returns: ['Thursday', 'Friday']
print(f"Slice [3:] (from index 3 to end): {days[3:]}")

# ------------------------------------------------------- #

# Slice the whole list (creates a copy)
print(f"Slice [:] (full copy): {days[:]}")