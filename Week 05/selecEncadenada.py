print("\n========== INGRESO DE DATOS ==========")

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese un número entero: "))
num3 = int(input("Ingrese un número entero: "))

if (num1 >= num2 and num1 >= num3):
    mayor = num1
elif (num2 >= num1 and num2 <= num3):
        mayor = num2
        print("Está en el rango de diez primeros números")
elif (num3 >= num1 and num3 >= num2):
        mayor = num3

print(f"El mayor número es: {mayor}")