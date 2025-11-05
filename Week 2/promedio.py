print("===== CALCULO DE PROMEDIO FINAL =====") # Mostramos el título del programa

c1 = float(input("Ingrese la nota del C1: ")) # Nota del consolidad 1
ep = float(input("Ingrese la nota de la Evalución parcial: ")) # Nota de la evaluación parcial
c2 = float(input("Ingrese la nota del C2: ")) # Nota del consolidad 2
ef = float(input("Ingrese la nota de la evalución final: ")) # Nota de la evaluación final
pf = (c1 * 0.20) + (ep * 0.25) + (c2 * 0.20) + (ef * 0.35) # Promedio final

print(f"El promedio final es: {pf:.2f}") # Mostramos el promedio final con dos decimales
