# a)
print("="*50) # Imprimimos una linea de separación
nombrePersona = input("Ingrese el nombre de la persona: ") # Ingresamos el nombre de la persona
apellidoPersona = input("Ingrese el apellido de la persona: ") # Ingresamos el apellido de la persona

nombreCompleto = nombrePersona + " " + apellidoPersona # Concatenamos el nombre y apellido

print("="*50) # Imprimimos una linea de separación
print(f"Nombre completo: {nombreCompleto}") # Mostramos el nombre completo

#b)
print("="*50) # Imprimimos una linea de separación
print(f"Longitud de cadena: {len(nombreCompleto)}") # Mostramos la longitud de la cadena

#c)
print("="*50) # Imprimimos una linea de separación
print("\nExtraer dos primeras letras") # Mostramos el mensaje
# Extraer desde la posición cero (primera letra) hasta dos (antes de la letra)
print(f"{nombreCompleto[0:2]}") # Mostramos las dos primeras letras

#d)
print("="*50) # Imprimimos una linea de separación
print(f"{'j' in (nombreCompleto)}") # Verificamos si 'j' está en el nombre completo
print(f"{'ab' in nombreCompleto}") # Verificamos si 'ab' está en el nombre completo

#e)
print("="*50) # Imprimimos una linea de separación
nombrePrimerMayusc = nombreCompleto.capitalize() # Capitalizamos la primera letra
print(f"Primera letra mayuscula: {nombrePrimerMayusc}") # Mostramos la primera letra mayúscula

nombreMayusc = nombreCompleto.upper() # Convertimos todo a mayúsculas
print(f"Todo Mayuscula: {nombreMayusc}") # Mostramos todo en mayúsculas

nombreMinusc = nombreCompleto.lower() # Convertimos todo a minúsculas
print(f"Todo Minuscula: {nombreMinusc}") # Mostramos todo en minúsculas
