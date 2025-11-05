print("\n========== MENÚ ==========\n") # Título del programa

print("1. Sopa Wantan\n2. Arroz Chaufa\n3. Refresco\n4. Postre\n") # Menú del restaurante

print("\n========== INGRESO DE DATOS ==========\n") # Título del ingreso de datos
precioSopa = float(input("Ingrese el precio de la Sopa Wantan: S/. ")) # Precio de la Sopa Wantan
cantSopa = int(input("Ingrese la cantidad de Sopa Wantan: ")) # Cantidad de Sopa Wantan

precioArroz = float(input("Ingrese el precio del Arroz Chaufa: S/. ")) # Precio del Arroz Chaufa
cantArroz = int(input("Ingrese la cantidad de Arroz Chaufa: ")) # Cantidad de Arroz Chaufa

precioRefresco = float(input("Ingrese el precio del Refresco: S/. ")) # Precio del Refresco
cantRefresco = int(input("Ingrese la cantidad de Refresco: ")) # Cantidad de Refresco

precioPostre = float(input("Ingrese el precio del Postre: S/. ")) # Precio del Postre
cantPostre = int(input("Ingrese la cantidad de Postre: ")) # Cantidad de Postre

subTotalSopa = precioSopa * cantSopa # Subtotal de la Sopa Wantan
subTotalArroz = precioArroz * cantArroz # Subtotal del Arroz Chaufa
subTotalRefresco = precioRefresco * cantRefresco # Subtotal del Refresco
subTotalPostre = precioPostre * cantPostre # Subtotal del Postre

montoPagar = subTotalSopa + subTotalArroz + subTotalRefresco + subTotalPostre # Monto total a pagar

print("\n========== FACTURA ==========\n") # Título de la factura
print(f"El subtotal de la Sopa Wantan es: S/. {subTotalSopa:.2f}") # Muestra el subtotal de la Sopa Wantan
print(f"El subtotal del Arroz Chaufa es: S/. {subTotalArroz:.2f}") # Muestra el subtotal del Arroz Chaufa
print(f"El subtotal del Refresco es: S/. {subTotalRefresco:.2f}") # Muestra el subtotal del Refresco
print(f"El subtotal del Postre es: S/. {subTotalPostre:.2f}") # Muestra el subtotal del Postre
print(f"El monto total a pagar es: S/. {montoPagar:.2f}") # Muestra el monto total a pagar

print("\n========== FIN DEL PROGRAMA ==========\n") # Fin del programa