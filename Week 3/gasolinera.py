print("\n========== INGRESO DE DATOS ==========\n") # Título del programa

conversion = 4 # Litros por galón

galonesComprados = int(input("Ingrese la cantidad de galones: ")) # Cantidad de galones comprados
precioLitros = float(input("Ingrese el precio de la gasolina por litro: ")) # Precio por litro

litrosDespachados = galonesComprados * conversion # Conversión de galones a litros
costoTotal = litrosDespachados * precioLitros # Cálculo del costo total

print("\n========== REPORTE DE PAGO ==========\n") # Título del reporte
print(f"Galones despachados: {galonesComprados}") # Muestra la cantidad de galones despachados
print(f"Precio por litro: S/. {precioLitros:.2f}") # Muestra el precio por litro
print(f"Total a pagar: S/. {costoTotal:.2f}") # Muestra el total a pagar

print("\n========== FIN DEL PROGRAMA ==========\n") # Fin del programa