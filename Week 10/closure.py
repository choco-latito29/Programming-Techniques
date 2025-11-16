# --- File: closure.py ---
# This program demonstrates a 'closure'.
# A closure occurs when a nested (inner) function
# remembers and has access to the variables from the
# scope of the (outer) function that contained it,
# even after the outer function has finished executing.

print("=" * 50)


def outer_function(n1):
    # 'n1' is a local variable in the 'outer_function's scope.

    def inner_function(n2):
        # 'inner_function' can access 'n2' (its own argument)
        # and also 'n1' (from the outer scope).
        print("", n2 * n1)

    # The outer function returns the 'inner_function' *object* itself,
    # not the result of calling it.
    return inner_function


# --- How this is executed ---

# 1. outer_function(5) is called first.
#    - It sets n1 = 5.
#    - It returns the 'inner_function' object.
#    - This returned function "remembers" that n1 is 5.

# 2. (3) is then called on the function that was just returned.
#    - This is the same as calling inner_function(3).
#    - It sets n2 = 3.
#    - It runs the print: 3 * 5 = 15

outer_function(5)(3)