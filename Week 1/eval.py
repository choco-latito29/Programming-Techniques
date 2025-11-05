print("\n***Ejemplo 6: Uso de Eval****\n") # Titulo del programa
# Ejemplo 6: Los valores de variable 1 y variable 2 son caracteres y con eval le convierte a númerico

variable1 = eval(input("Ingrese el valor de variable a: ")) # con eval lo convierte a número
variable2 = eval(input("Ingrese el valor de variable b: ")) # con eval lo convierte a número
variable3 = variable1 + variable2 # suma las variables

print(f"El resultado es: {variable3}") # Ahora si se suma, usa coma
print(f"El resultado es: {str(variable3)}") # con str() se convierte la variable c en cadena.