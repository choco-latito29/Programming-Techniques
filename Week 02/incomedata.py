# Ingresar nombre, precio y cantidad de producto, tambien un descuento
# Calcular el monto de pago

print("\n========== INGRESO DE DATOS ==========\n")

nombreProduc = input("Ingrese el nombre del producto: ") # Ingresamos el nombre del producto

precioProduc = float(input("Ingrese el precio del producto: ")) # Ingresamos el precio del producto

cantidadProduc = int(input("Ingrese la cantidad del producto: ")) # Ingresamos la cantidad del producto

porcentajeDcto = float(input("Ingrese el porcentaje de descuento: ")) # Ingresamos el porcentaje de descuento

montoBruto = precioProduc * cantidadProduc # Calculamos el monto bruto
montoDcto = montoBruto * (porcentajeDcto / 100) # Calculamos el monto de descuento
montoPago = montoBruto - montoDcto # Calculamos el monto a pagar

print("\n========== REPORTE ==========\n") # Imprimimos el titulo del reporte
print(f"El Monto Bruto es: {montoBruto}") # Mostramos el monto Bruto
print(f"El Monto de Descuento es: {montoDcto}") # Mostramos el monto de Descuento
print(f"El Monto a Pagar es: {montoPago}") # Mostramos el monto a Pagar
