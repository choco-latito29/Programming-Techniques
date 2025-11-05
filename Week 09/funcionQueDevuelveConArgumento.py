print("=" * 50)

def sumar(n1, n2):

    sum = n1 + n2

    return sum

def ejecutar():

    num1 = eval(input("Ingrese el primer numero: "))
    num2 = eval(input("Ingrese el segundo numero: "))

    s = sumar(num1, num2)

    print("\n========== REPORTE ==========\n")
    print(f"La suma es: {s}")
    print("=" * 50)

ejecutar()