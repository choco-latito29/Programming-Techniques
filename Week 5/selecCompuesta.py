print("\n========== INGRESO DE DATOS ==========")

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

if (a > 0 and b > 0):
    c = a + b

    print(f"El valor de la suma es : {c}")
else:
    c = a * b

    print(f"El valor de la multiplicación es: {c}")