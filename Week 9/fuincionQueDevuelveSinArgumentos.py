print("=" * 50)

def sumar(n1, n2):
    sum1 = eval(input("Ingrese el primer numero: "))
    sum2 = eval(input("Ingrese el segundo numero: "))

    sum = n1 + n2

    return sum

def ejecutar():

    s = sumar()

    print("\n========== REPORTE ==========\n")
    print(f"La suma es: {s}")
    print("=" * 50)

ejecutar()