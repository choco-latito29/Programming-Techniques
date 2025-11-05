print("====== DATOPS PARA EL AUTO 1 ======") # Mostramos los datos para el auto 1
auto1 = {
    "placaAuto1": input("Ingrese la placa del auto 1: "), # Placa del auto 1
    "modeloAuto1": input("Ingrese el modelo del auto 1: "), # Modelo del auto 1
    "colorAuto1": input("Ingrese el color del auto 1: ") # Color del auto 1
}

print("====== DATOS PARA EL AUTO 2 ======") # Mostramos los datos para el auto 2
auto2 = {
    "placaAuto2": input("Ingrese la placa del auto 2: "), # Placa del auto 2
    "modeloAuto2": input("Ingrese el modelo del auto 2: "), # Modelo del auto 2
    "colorAuto2": input("Ingrese el color del auto 2: ") # Color del auto 2
}

print("====== DATOS PARA EL AUTO 3 ======") # Mostramos los datos para el auto 3
auto3 = {
    "placaAuto3": input("Ingrese la placa del auto 3: "), # Placa del auto 3
    "modeloAuto3": input("Ingrese el modelo del auto 3: "), # Modelo del auto 3
    "colorAuto3": input("Ingrese el color del auto 3: ") # Color del auto 3
}

# Diccionario de Autos
diccionarioAuto = {
    "auto N°1": auto1, # Datos del auto 1
    "auto N°2": auto2, # Datos del auto 2
    "auto N°3": auto3  # Datos del auto 3
}

print("====== DATOS DE TODOS LOS AUTOS ======") # Mostramos los datos de todos los autos
print(f"{diccionarioAuto}") # Mostramos el diccionario de autos