print("\n========== INGRESO DE DATOS ==========")

num = int(input("Ingrese un número entero: "))

if (num > 0):
    if (num >= 1 and num <= 10):
        print("Está en el rango de diez primeros números")
    else:
        print("Está más del rango de los diez primeros números")
else:
    print("[ERROR] el número no es mayor a cero")