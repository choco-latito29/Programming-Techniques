print("=" * 50)

def sumar():
    num1 = eval(input("Ingrese el primer numero: "))
    num2 = eval(input("Ingrese el segundo numero: "))

    sum = num1 + num2

    print("\n========== REPORTE ==========\n")
    print(f"La suma es: {sum}")
    print("=" * 50)

def ejecutar():
   sumar()

ejecutar()