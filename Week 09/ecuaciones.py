print("=" * 50)

def leeDatoE():
    dato = int(input(""))

    return dato

def ecuaciones():
    print("Ingrese el valor de X: ")

    x = leeDatoE()

    if (x <= 0):
        y = (x ** 2) + 5
    elif (x > 0 and x < 2):
        y = (3 * x) - 1
    elif (x >= 2):
        y = (x ** 2) - (4 * x) + 5

    print(f"El valor de Y es: {y}")

def ejecutar():
    ecuaciones()

ejecutar() 