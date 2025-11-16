# --- File: function_call_error.py ---
# This program demonstrates a common TypeError.

print("=" * 50)

# The function is defined to REQUIRE two arguments, n1 and n2
def sumar(n1, n2):
    # These lines ask the user for input
    sum1 = eval(input("Ingrese el primer numero: "))
    sum2 = eval(input("Ingrese el segundo numero: "))

    # Logical Error: The code tries to add n1 + n2 (the arguments it expected)
    # instead of adding the variables it just got from the user (sum1 + sum2).
    sum = n1 + n2

    return sum

def ejecutar():

    # --- ERROR OCCURS HERE ---
    # The 'sumar' function was called with 0 arguments (it needs 2).
    # This line will cause:
    # TypeError: sumar() missing 2 required positional arguments: 'n1' and 'n2'
    s = sumar()

    print("\n========== REPORTE ==========\n")
    print(f"La suma es: {s}")
    print("=" * 50)

ejecutar()