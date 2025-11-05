print("\n========== INGRESO DE DATOS ==========\n") # Titulo del programa

a = int(input("Ingrese el primer número (a): ")) # Entrada del primer número
b = int(input("Ingrese el segundo número (b): ")) # Entrada del segundo número
c = int(input("Ingrese el tercer número (c): ")) # Entrada del tercer número

print("\n========== REPORTE ==========\n") # Titulo del reporte

if a == b == c: # Verifica si los tres números son iguales
    print("Los tres números son iguales.") # Mensaje si los tres números son iguales
else: # Si no son iguales, encuentra el mayor
    mayor = a # Asume que 'a' es el mayor inicialmente

    if b > mayor: # Verifica si 'b' es mayor que el actual mayor
        mayor = b # Actualiza el mayor a 'b'
    if c > mayor: # Verifica si 'c' es mayor que el actual mayor
        mayor = c # Actualiza el mayor a 'c'

    if mayor == a and mayor == b: # Verifica si hay un empate entre dos números
        print(f"El mayor es A y B = {mayor}") # Mensaje si 'a' y 'b' son iguales y mayores
    elif mayor == a and mayor == c: # Verifica si hay un empate entre dos números
        print(f"El mayor es A y C = {mayor}") # Mensaje si 'a' y 'c' son iguales y mayores
    elif mayor == b and mayor == c: # Verifica si hay un empate entre dos números
        print(f"El mayor es B y C = {mayor}") # Mensaje si 'b' y 'c' son iguales y mayores
    elif mayor == a: # Verifica si 'a' es el mayor
        print(f"El mayor es A = {mayor}") # Mensaje si 'a' es el mayor
    elif mayor == b: # Verifica si 'b' es el mayor
        print(f"El mayor es B = {mayor}") # Mensaje si 'b' es el mayor
    else: # Si no es ninguno de los anteriores, 'c' es el mayor
        print(f"El mayor es C = {mayor}") # Mensaje si 'c' es el mayor
