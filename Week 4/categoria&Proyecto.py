print("\n========== INGRESO DE DATOS ==========\n")

montobase = float(input("Ingrese el monto base en dolares: "))

print("\nCategoria\n\n1. Categoria V\n2. Categoria R\n3. Categoria P\n4. Categoria A\n5. Categoria L\n")
category = input("Ingrese la categoria: ")

print("\nTipo de Proyecto\n\n1. Vivienda\n2. Recreativo\n3. Piscina\n4. Auditorio\n5. Edificio\n")
proyect = input("Ingrese el tipo de proyecto: ")

descuento = 0

if category == 1 and proyect == 1:
    descuento = 5
elif category == 2 and proyect == 2:
    descuento = 10
elif category == 3 and proyect == 2:
    descuento = 15
elif category == 4 and proyect == 2:
    descuento = 20
elif category == 5 and proyect == 5:
    descuento = 25
else:
    descuento = 0

dolartosoles = float(input("\nIngrese el tipo de cambio: "))

montoBaseSoles = montobase / dolartosoles
montoDescuento = (montoBaseSoles * descuento) / 100
montoPagar = montoBaseSoles - montoDescuento

print("\n========== RESULTADOS ==========\n")
print(f"El monto Base en soles es: {montoBaseSoles:.2f}")
print(f"El monto con descuento es: {montoDescuento:.2f}")

print("\nFin del Programa\n")