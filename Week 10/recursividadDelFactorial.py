def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

def ejecutar():
    while True:
        num = int(input("Ingrese un número para factorial: "))

        if (num < 0):
            print("[ERROR] Vuelva a ingresar...")
        else:
            break

    rpta = factorial(num)

    print(f"El factorial es: {rpta}")

ejecutar()