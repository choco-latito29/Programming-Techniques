print("\n========== INGRESO DE DATOS ==========\n") # Título del programa

n = int(input("Ingrese un número: ")) # Solicita al usuario que ingrese un número entero

if n < 2: # Verifica si el número es menor que 2
    print(n, "NO es primo (los primos son mayores o iguales a 2).") # Informa que no es primo
else: # Si el número es 2 o mayor, procede a verificar si es primo
    i = 2 # Inicializa el divisor en 2
    es_primo = True # Asume que el número es primo hasta que se demuestre lo contrario

    while i < n: # Recorre todos los números desde 2 hasta n-1
        if n % i == 0: # Verifica si n es divisible por i
            es_primo = False # Si es divisible, no es primo
            break # Sale del bucle
        i += 1 # Incrementa el divisor

    if es_primo: # Si es primo, informa al usuario
        print(n, "ES primo.") # Si es primo, informa al usuario
    else: # Si no es primo, informa al usuario y el divisor encontrado
        print(n, "NO es primo. Es divisible por", i) # Si no es primo, informa al usuario y el divisor encontrado
