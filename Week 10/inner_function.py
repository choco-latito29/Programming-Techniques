# --- File: inner_function.py ---
# This program demonstrates a nested (inner) function
# that is called by its parent (outer) function.

print("=" * 50)


def outer_function():
    # 'inner_function' is defined inside the scope of 'outer_function'
    def inner_function():
        return "Example of an inner function"

    # --- Key Difference ---
    # Unlike a closure, the outer function CALLS the inner function (note the '()')
    # and returns its RESULT (the string).
    return inner_function()


# 1. outer_function() is called.
# 2. Inside, inner_function() is defined.
# 3. inner_function() is called and returns its string.
# 4. outer_function() returns that same string.
# 5. print() displays the string.
print(outer_function())