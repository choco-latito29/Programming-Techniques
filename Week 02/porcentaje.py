print("\n========== INGRESO DE DATOS ==========\n") # Imprimimos el titulo del programa

cantHombres = int(input("Ingrese la cantidad de hombres: ")) # Ingresamos la cantidad de hombres
cantMujeres = int(input("Ingrese la cantidad de mujeres: ")) # Ingresamos la cantidad de mujeres

totalAlumnos = cantHombres + cantMujeres # Calculamos el total de alumnos

porcentajeHombres = round((cantHombres * 100) / totalAlumnos) # Calculamos el porcentaje de hombres
porcentajeMujeres = round((cantMujeres * 100) / totalAlumnos) # Calculamos el porcentaje de mujeres

print("\n========== REPORTE ==========") # Imprimimos el titulo del reporte
print(f"El porcentaje de Hombres es: {porcentajeHombres}%") # Mostramos el porcentaje de hombres
print(f"El porcentaje de Mujeres es: {porcentajeMujeres}%") # Mostramos el porcentaje de mujeres
