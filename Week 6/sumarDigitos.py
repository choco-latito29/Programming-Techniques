num = 0 

while num <= 0:
    entrada = int(input("Ingrese un número: "))

    if (entrada <= 0):
        print("[ERROR] El número debe ser mayor a 0.... Vuelva a intentar")

suma = 0
num_proceso = num 

while num_proceso > 0:
    digito = num_proceso % 10
    suma = suma + digito
    num_proceso = num_proceso // 10

print("\n--- REPORTE ---")
print(f"El número ingresado fue: {num}")
print(f"La suma de sus dígitos es: {suma}")