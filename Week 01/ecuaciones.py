import math # Importa la librería matemática

print('\n', "==== Ecuaciones ===", '\n') # Título del programa

x = eval(input("Ingrese x: ")) # Solicita al usuario que ingrese el valor de x

potencial1 = pow(x + 3, 2) # Calcula (x + 3) elevado al cuadrado usando la función pow de la librería math
raiz = math.sqrt(x + 5) # Calcula la raíz cuadrada de (x + 5) usando la función sqrt de la librería math
potencia2 = pow(x, 2/3) # Calcula x elevado a la potencia de 2/3 usando la función pow de la librería math
z = (potencial1 + x + raiz) / potencia2 + 1 # Calcula el valor de z según la fórmula dada

print("\nLa ecuacion es: ", z, "\n") # Muestra el resultado de la ecuación al usuario