a = int(input("Ingrese el primer número (a): ")) # Ingresamos el primer número.
operador = input("Ingrese el operador (+, -, *, /): ") # Ingresamos el operador (Operación a realizar)
b = int(input("Ingrese el segundo número (b): ")) # Ingresamos el segundo número.

sulucion = "" # Enviamos un resultao vacio.

if operador == "+": # Evaluamos el operador y realizamos la operación correspondiente.
    resultado = a + b # Realizamos la suma.
    print(f"{a} + {b} = {resultado}") # Imprimimos el resultado.
elif operador == "-": # Evaluamos si el operador es resta.
    resultado = a - b # Realizamos la resta.
    print(f"{a} - {b} = {resultado}") # Imprimimos el resultado.
elif operador == "*": # Evaluamos si el operador es multiplicación.
    resultado = a * b # Realizamos la multiplicación.
    print(f"{a} * {b} = {resultado}") # Imprimimos el resultado.
elif operador == "/": # Evaluamos si el operador es división.
    if b != 0: # Verificamos que el divisor no sea cero.
        resultado = a / b # Realizamos la división.
        print(f"{a} / {b} = {resultado}") # Imprimimos el resultado.
    else: # Si el divisor es cero, mostramos un mensaje de error.
        resultado = "Error: División por cero" # Asignamos un mensaje de error a resultado.