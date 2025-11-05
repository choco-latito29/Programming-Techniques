from datetime import datetime # Para trabajar con fechas y horas
print("="*50) # Imprimimos una linea de separación
numero = 11.5497 # Definimos un número decimal

print(f"Con dos decimales: {numero:.2f}") # Mostramos el número con dos decimales
print(f"Completo: {numero:f}") # Mostramos el número completo
print(f"Redondear: {round(numero)}") # Redondeamos el número
print(f"Numero a cadena: {str(numero)}") # Convertimos el número a cadena

fechaAhora = datetime.now() # Obtenemos la fecha y hora actual
print(f"Mostrar fecha actual: {fechaAhora}") # Mostramos la fecha actual

hora = fechaAhora.time() # Obtenemos la hora actual
print(f"Mostrar hora actual: {hora}") # Mostramos la hora actual

año = fechaAhora.year # Obtenemos el año actual
mes = fechaAhora.month # Obtenemos el mes actual
dia = fechaAhora.day # Obtenemos el día actual

print(f"Mostrar Año: {año}") # Mostramos el año actual
print(f"Mostrar Mes: {mes}") # Mostramos el mes actual
print(f"Mostrar Día: {dia}") # Mostramos el día actual