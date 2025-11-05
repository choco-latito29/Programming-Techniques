# Autor: TuApellidoNombre (# es para comentario de una linea)

"""
( comillas es para comentarios
de mas de una linea)
""" # Explicacion del programa

print('\n', "==== Cálculos Básicos ===", '\n') # Titulo del programa

print("Ingresa tu nombre: ") # Solicita el nombre del usuario
TuNombre = input() # Guarda el nombre del usuario

base = float(input("Ingrese base: ")) # Solicita y guarda la base

altura = float(input("Ingrese altura: ")) # Solicita y guarda la altura

Area = (base * altura)/2 # Calcula el area del triangulo

#La coma separa string, y numericos
print(f'\n{TuNombre} Calculó el area: {Area}\n') # Muestra el resultado del area