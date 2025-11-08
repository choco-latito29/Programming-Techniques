import Bookshops.lecturaDatos as lector
import Bookshops.utilitarios as util
import Bookshops.tarifas as tarifas

total_facturas = 0
cont_categoria_A = 0
cont_categoria_C = 0
acum_total_pagar = 0.0
acum_montos_mayores_600 = 0.0

def reportar():
    print("\n======== REPORTE GENERAL ========")
    print(f"Cantidad total de facturas calculadas: {total_facturas}")
    print(f"Cantidad de veces con categoría 'A': {cont_categoria_A}")
    print(f"Cantidad de veces con categoría 'C': {cont_categoria_C}")
    print(f"Acumulado de montos totales a pagar: S/ {acum_total_pagar:.2f}")
    print(f"Acumulado de montos >= S/ 600: S/ {acum_montos_mayores_600:.2f}")
    print("=" * 35)

def procesar():
    global total_facturas, cont_categoria_A, cont_categoria_C
    global acum_total_pagar, acum_montos_mayores_600

    print("\n--- 1. Cálculo de Factura ---")
    consumo_kwh = lector.leerFloatPositivo("Ingrese Consumo (kWh): ")
    categoria = lector.leerCategoria("Ingrese Categoría (A, B, C, D, E): ")
    tipo_cambio = lector.leerFloatPositivo("Ingrese Tipo de Cambio (Soles x USD): ")

    tarifa_base_usd, porc_penalidad = tarifas.getDatosPorCategoria(categoria)

    monto_base_usd = consumo_kwh * tarifa_base_usd
    monto_base_soles = monto_base_usd * tipo_cambio
    monto_penalidad_soles = monto_base_soles * porc_penalidad

    total_pagar_soles = monto_base_soles + monto_penalidad_soles

    total_facturas += 1
    acum_total_pagar += total_pagar_soles

    if (categoria == 'A'):
        cont_categoria_A += 1
    elif (categoria == 'C'):
        cont_categoria_C += 1

    if (total_pagar_soles >= 600):
        acum_montos_mayores_600 += total_pagar_soles

    print("\n--- Reporte de Factura ---")
    if consumo_kwh > 500:
        print("Mensaje: Consumo excesivo, riesgo de sobrecarga.")
    
    print(f"Monto Base en Soles: S/ {monto_base_soles:.2f}")
    print(f"Monto de Penalidad: S/ {monto_penalidad_soles:.2f}")
    print(f"Total a Pagar en Soles: S/ {total_pagar_soles:.2f}")

def menu():
    print("\n======== MENÚ PRINCIPAL ========")
    print("1. Calcular Factura")
    print("2. Reportar Contadores y Acumuladores")
    print("3. Salir")

    op = lector.leerOpcionMenu("Ingrese una opción: ", 1, 3)

    match op:
        case 1:
            procesar()
        case 2:
            reportar()
        case 3:
            util.salir()

    return op

def ejecutar():
    while True:
        opcion = menu()
        if opcion == 3:
            break

ejecutar()