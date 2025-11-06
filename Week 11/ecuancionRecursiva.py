import Bookshops.recursivas as recursv

print("=" * 50)

def calcular():
    while True:
        n = int(input("Ingrese el valor de n: "))

        if (n < 0):
            print("[ERROR] vuelva a ingresar")
        else:
            break

    while True:
        a = float(input("Ingrese el valor de a: "))

        if (a < 0):
            print("[ERROR] vuelva a ingresar")
        else:
            break

    while True:
        b = float(input("Ingrese el valor de b: "))

        if (b < 0):
            print("[ERROR] vuelva a ingresar")
        else:
            break

    fact = recursv.factorial(n)

    mult = recursv.multiplica(a, b)

    resta = fact - mult

    if (n != 0):
        z = resta/n
        print(f"El resultado valor de la ecuacion Z es: {z}")
    else:
        print("[ERROR] No se puede dividir por cero")

    print(f"El valor de factorial de {n} es: {fact}")
    print(f"El valor de la multiplicacion de {a} y {b} es: {resta}")

calcular()