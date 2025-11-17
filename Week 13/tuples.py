# --- File: tuples.py ---
# This program demonstrates how to create Tuples in Python.
# Tuples are IMMUTABLE sequences (they cannot be changed after creation).

# Example 1: A tuple with mixed data types (strings, float, int)
tuple_example_1 = ("Juan Perez", "Ana", 10.8, 5)

# Example 2: A tuple containing other structures
# Note: While the tuple itself is immutable, the list inside it IS mutable.
tuple_example_2 = (1, 3, ["Java", "Python", "SQL"], {"h", "o", "l", "a"})

print(f"Tuple Example 1: {tuple_example_1}")
print(f"Tuple Example 2: {tuple_example_2}")