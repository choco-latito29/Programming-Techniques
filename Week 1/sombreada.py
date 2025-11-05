# Carpeta: Programas Semana 01
# Nombre de Programa: ProgramaPropuesto2Pieza

# Este programa calcula el área sombreada de una pieza mecánica a partir del lado de un cuadrado.
# El área es el área del cuadrado menos el área de un círculo.
import math

print("==== Cálculo del Área de una Plantilla ====")

# Solicitar la longitud del lado del cuadrado
lado_cuadrado = float(input("Ingrese la longitud del lado del cuadrado: "))

# El área del cuadrado es lado * lado
area_cuadrado = lado_cuadrado * lado_cuadrado

# El diámetro del círculo es igual al lado del cuadrado, por lo que el radio es lado / 2
radio = lado_cuadrado / 2

# El área del círculo es pi * radio^2
area_circulo = math.pi * (radio ** 2)

# El área sombreada es el área del cuadrado menos el área del círculo
area_sombreada = area_cuadrado - area_circulo

# Imprimir el resultado
print(f"El área sombreada de la plantilla es: {area_sombreada}")