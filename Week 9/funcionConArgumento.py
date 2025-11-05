print("=" * 50)

def sumar(n1, n2):

    sum = n1 + n2

    print("\n========== REPORTE ==========\n")
    print(f"La suma es: {sum}")
    print("=" * 50)

def ejecutar():

    num1 = eval(input("Ingrese el primer numero: "))
    num2 = eval(input("Ingrese el segundo numero: "))

    sumar(num1, num2)

ejecutar()