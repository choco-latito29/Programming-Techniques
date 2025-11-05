print("\n========== INGRESO DE DATOS ==========\n")

totalPrecio = 0

for i in range (10):
    while True:
        precioProduc = float(input(f"Ingrese precio del producto {i + 1}: "))

        if (precioProduc <= 0):
            print("[ERROR] vuelva a ingresar")
        else:
            break

    totalPrecio = totalPrecio + precioProduc

if totalPrecio > 200:
    dcto = 0.15
else:
    dcto = 0

montoDcto = totalPrecio * dcto
montoPago = totalPrecio - montoDcto

print("\n========== REPORTE ==========\n")
print(f"El monto a pagar es: {totalPrecio}")
print(f"El monto descuento es: {montoDcto}")
print(f"El monto a pagar es: {montoPago}")