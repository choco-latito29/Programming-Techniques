dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# RECORRIENDO LA LISTA
for i in range(len(dias)):
    print(f"Los dias son: {dias[i]}")

# ------------------------------------------------------- #
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
turno = [1, 2]

# Concatenar Lista
horario = dias + turno
print(f"La concatenación es: {horario}")

# ------------------------------------------------------- #
Dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# Rebanada de Lista
Dias[1:3]
print(f"Desde la posición 1 hasta la 3 es: {Dias}")

# ------------------------------------------------------- #
Dias[:3]
print(f"Desde la posición 0 hasta la 3 es: {Dias}")

# ------------------------------------------------------- #
Dias[3:]
print(f"Desde la posición 3 hasta el final es: {Dias}")

# ------------------------------------------------------- #
Dias[:]
print(f"Copiados de la lista es: {Dias}")