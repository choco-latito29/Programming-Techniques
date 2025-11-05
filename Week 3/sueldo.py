print("\n========== INGRESO DE DATOS ==========\n") # Título del programa

porctComision = 0.08 # Porcentaje de comisión

sueldoBase = float(input("Ingrese el sueldo base: S/. ")) # Sueldo base
importeVentas = float(input("Ingrese importe de ventas: S/. ")) # Importe de ventas

montoComision = importeVentas * porctComision # Cálculo del monto de comisión
sueldoNeto = sueldoBase + montoComision # Cálculo del sueldo neto

print("\n========== REPORTE DE DATOS ==========\n") # Título del reporte
print(f"Porcentaje de comisión: {porctComision}%") # Muestra el porcentaje de comisión
print(f"El monto de comisión es: S/. {montoComision}") # Muestra el monto de comisión
print(f"El sueldo neto es: S/. {sueldoNeto}") # Muestra el sueldo neto

print("\n========== FIN DEL PROGRAMA ==========\n") # Fin del programa