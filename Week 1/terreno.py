# Este programa calcula el área de un terreno con forma de trapecio rectángulo.

print("==== Cálculo del Área de un Terreno (Trapecio) ====")

# Solicitar las longitudes A y B al usuario
longitud_A = float(input("Ingrese la longitud A: "))
longitud_B = float(input("Ingrese la longitud B: "))

# Calcular el área del trapecio
# Las bases son A y B, y la altura es B.
area_trapecio = ((longitud_A + longitud_B) / 2) * longitud_B

# Imprimir el resultado
print(f"El área total del terreno es: {area_trapecio}")