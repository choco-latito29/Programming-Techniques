print("\n========== INGRESO DE DATOS ==========\n") # Titulo del programa

montoSoles = float(input("Ingrese el monto en soles: ")) # Monto en soles a convertir

tipoCambioDolar = float(input("Ingrese el tipo de cambio del dólar: ")) # Tipo de cambio del dólar
tipocambioEuro = float(input("Ingrese el tipo de cambio del euro: ")) # Tipo de cambio del euro

solestoDolares = montoSoles * tipoCambioDolar # Conversion de soles a dolares
solestoEuros = montoSoles * tipocambioEuro # Conversion de soles a euros

print("\n========== REPORTE ==========\n") # Titulo del reporte
print(f"El monto en dolares es: {solestoDolares:.2f} $") # Monto en dolares con 2 decimales
print(f"El monto en euros es: {solestoEuros:.2f} €") # Monto en euros con 2 decimales