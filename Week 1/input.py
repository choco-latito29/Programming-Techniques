print("\n****Ejemplo 5: Uso de Input***\n")
# Ejemplo 5: Los valores de variable 1 y variable 2 son caracteres (al ser ingresado por teclado)

variable1 = input("Ingrese el valor de variable a: ") # input lo recibe como texto y no número y lo almacena en variable1
variable2 = input("Ingrese el valor de variable b: ") # input lo recibe como texto y no número y lo almacena en variable2
variable3 = variable1 + variable2 # como son recibidos como caracter, no se suma, se concatenan

print(f"El resultado es: {variable3}")