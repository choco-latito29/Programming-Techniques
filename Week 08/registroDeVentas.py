cantidad_clientes_F = 0
cantidad_ventas_100a1000 = 0
cantidad_ventas_cliente_M = 0
acumulador_total_monto_ventas = 0

# Variables para el reporte
ventas = []  # Lista para almacenar cada venta como diccionario
acumulador_importe_tipo2 = 0
acumulador_importe_neto_M = 0
cantidad_clientes_regulares = 0
acumulador_importe_regulares = 0
mejor_cliente = None
mayor_importe = 0


while True:
    print("\n========== MENU PRINCIPAL ==========\n")
    print("1. Registrar Venta")
    print("2. Reporte de Ventas")
    print("3. Salir")

    while True:
        op = int(input("Ingrese una opción del menú: "))

        if op < 1 or op > 3:
            print("[ERROR] Vuelve a ingresar")
        else:
            break

    match op:
        case 1:
            while True:
                print("\n========== TIPO DE CLIENTE ==========\n")
                print("1. Regular")
                print("2. VIP")
                tipo_cliente = int(input("Seleccione tipo de cliente (1-Regular, 2-VIP): "))
                if tipo_cliente not in [1, 2]:
                        print("[ERROR] Tipo de cliente inválido.")
                        continue
                genero = input("Ingrese género del cliente (M/F): ").strip().upper()
                if genero not in ["M", "F"]:
                        print("[ERROR] Género inválido.")
                        continue
                print("\n========== TIPO DE PLAN ==========\n")
                print("1. Básico (S/ 100 por mes)")
                print("2. Plus (S/ 200 por mes)")
                print("3. Elite (S/ 300 por mes)")
                tipo_plan = int(input("Seleccione tipo de plan (1-Básico, 2-Plus, 3-Elite): "))
                if tipo_plan not in [1, 2, 3]:
                        print("[ERROR] Tipo de plan inválido.")
                        continue
                meses = int(input("Ingrese cantidad de meses de membresía: "))
                if meses < 1:
                        print("[ERROR] Cantidad de meses inválida.")
                        continue
                    # Precios por plan
                precios = {1: 100, 2: 200, 3: 300}
                precio_base = precios[tipo_plan] * meses
                    # Descuentos
                if meses == 1:
                        descuento = 0
                elif 2 <= meses <= 5:
                       descuento = 0.05
                elif 6 <= meses <= 10:
                       descuento = 0.10
                else:
                        descuento = 0.15
                importe_neto = precio_base * (1 - descuento)
                    # Guardar venta
                venta = {
                        "tipo_cliente": tipo_cliente,
                        "genero": genero,
                        "tipo_plan": tipo_plan,
                        "meses": meses,
                        "importe_neto": importe_neto
                    }
                ventas.append(venta)
                    # Acumuladores y contadores
                acumulador_total_monto_ventas += importe_neto
                if genero == "F":
                    cantidad_clientes_F += 1
                    if 100 <= importe_neto <= 1000:
                        cantidad_ventas_100a1000 += 1
                    if genero == "M":
                        cantidad_ventas_cliente_M += 1
                        acumulador_importe_neto_M += importe_neto
                    if tipo_cliente == 2:
                        acumulador_importe_tipo2 += importe_neto
                    if tipo_cliente == 1:
                        cantidad_clientes_regulares += 1
                        acumulador_importe_regulares += importe_neto
                    if importe_neto > mayor_importe:
                        mayor_importe = importe_neto
                        mejor_cliente = venta
                    print(f"Venta registrada. Importe neto: S/ {importe_neto:.2f}")
                    break
        case 2:
                print("\n========== REPORTE DE VENTAS ==========\n")
                print(f"Cantidad de clientes de género femenino: {cantidad_clientes_F}")
                print(f"Cantidad de ventas entre S/ 100 y S/ 1000: {cantidad_ventas_100a1000}")
                print(f"Cantidad de ventas a clientes masculinos: {cantidad_ventas_cliente_M}")
                print(f"Acumulador total de todas las ventas: S/ {acumulador_total_monto_ventas:.2f}")
                print(f"Acumulador del importe neto de tipo 2 (VIP): S/ {acumulador_importe_tipo2:.2f}")
                if cantidad_clientes_regulares > 0:
                    promedio_regulares = acumulador_importe_regulares / cantidad_clientes_regulares
                else:
                    promedio_regulares = 0
                print(f"Promedio importe neto de clientes regulares: S/ {promedio_regulares:.2f}")
                if mejor_cliente:
                    print(f"Punto más alto (mejor cliente): Importe S/ {mayor_importe:.2f}, Tipo Cliente: {'Regular' if mejor_cliente['tipo_cliente']==1 else 'VIP'}, Género: {mejor_cliente['genero']}, Plan: {['Básico','Plus','Elite'][mejor_cliente['tipo_plan']-1]}, Meses: {mejor_cliente['meses']}")
                else:
                    print("No hay ventas registradas.")
        case 3:
            print("[VUELVA PRONTO] Saliendo del programa.........")

            break
