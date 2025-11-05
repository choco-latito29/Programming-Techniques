contadorAcciones = 0
contadorAccionesC = 0
contadorAccionesE = 0
AcumuladoPagarSoles = 0
AcumuladoPagarSolesB = 0
AcumuladoMontoTotal5K = 0

montoBase = int(input("Ingrese el monto base $: "))
tipoCambio = float(input("Ingrese el tipo de cambio $ => S: "))

while True:
    print("\n========== MENU DE OPCIONES ==========\n")
    print("1. Calcular Impuestos")
    print("2. Reportar Contador y Acumulados")
    print("3. Salir")

    while True:
        op = int(input("Ingrese una opción: "))

        if (op < 1 or op > 3):
            print("[ERROR] Vuelve a ingresar")
        else:
            break

    match op:
        case 1:
            while True:
                print("\n========== SUBMENU DE OPCIONES ==========\n")
                print("1. cATEGORIA A")
                print("2. Categoria B")
                print("3. Categoria C")
                print("4. Categoria D")
                print("5. Categoria E")

                while True:
                    op = int(input("Ingrese una categoria: "))

                    if (op < 1 or op > 5):
                        print("[ERROR] Vuelva a ingresar")
                    else:
                        break
                
                match op:
                    case 1:
                        contadorAcciones = contadorAcciones + 1  

                        Category = "A"
                        vehiculo = "Motocicleta"
                        dsto = 0.3

                        montoImpuesto = montoBase * dsto
                        montoTotal = montoBase + montoImpuesto
                        montoBaseSoles = montoBase * tipoCambio
                        montoTotalSoles = montoTotal * tipoCambio


                        print("\n========== REPORTE DE REGISTRO ==========\n")
                        print(f"La categoria es: {Category}")
                        print(f"El tipo de Vehiculo es: {vehiculo}")
                        print(f"El monto base en soles es: {montoBaseSoles:.2F}")
                        print(F"El monto de impuestos en soles es: {(montoBaseSoles * dsto):.2f}")
                        print(f"El monto total a pagar en soles es: {montoTotalSoles:.2f}")

                        AcumuladoPagarSoles = AcumuladoPagarSoles + montoTotalSoles                        

                        break
                    
                    case 2:
                        contadorAcciones = contadorAcciones + 1  

                        Category = "B"
                        vehiculo = "Auto Particular"
                        dsto = 0.5

                        montoImpuesto = montoBase * dsto
                        montoTotal = montoBase + montoImpuesto
                        montoBaseSoles = montoBase * tipoCambio
                        montoTotalSoles = montoTotal * tipoCambio


                        print("\n========== REPORTE DE REGISTRO ==========\n")
                        print(f"La categoria es: {Category}")
                        print(f"El tipo de Vehiculo es: {vehiculo}")
                        print(f"El monto base en soles es: {montoBaseSoles:.2F}")
                        print(F"El monto de impuestos en soles es: {(montoBaseSoles * dsto):.2f}")
                        print(f"El monto total a pagar en soles es: {montoTotalSoles:.2f}")

                        AcumuladoPagarSoles = AcumuladoPagarSoles + montoTotalSoles

                        AcumuladoPagarSolesB = AcumuladoPagarSolesB + montoTotalSoles

                        break

                    case 3:
                        contadorAcciones = contadorAcciones + 1  
                        contadorAccionesC = contadorAccionesC + 1

                        Category = "C"
                        vehiculo = "Camioneta"
                        dsto = 0.7

                        montoImpuesto = montoBase * dsto
                        montoTotal = montoBase + montoImpuesto
                        montoBaseSoles = montoBase * tipoCambio
                        montoTotalSoles = montoTotal * tipoCambio


                        print("\n========== REPORTE DE REGISTRO ==========\n")
                        print(f"La categoria es: {Category}")
                        print(f"El tipo de Vehiculo es: {vehiculo}")
                        print(f"El monto base en soles es: {montoBaseSoles:.2F}")
                        print(F"El monto de impuestos en soles es: {(montoBaseSoles * dsto):.2f}")
                        print(f"El monto total a pagar en soles es: {montoTotalSoles:.2f}")

                        AcumuladoPagarSoles = AcumuladoPagarSoles + montoTotalSoles

                        break

                    case 4:
                        contadorAcciones = contadorAcciones + 1  

                        Category = "D"
                        vehiculo = "Camion"
                        dsto = 0.10

                        montoImpuesto = montoBase * dsto
                        montoTotal = montoBase + montoImpuesto
                        montoBaseSoles = montoBase * tipoCambio
                        montoTotalSoles = montoTotal * tipoCambio


                        print("\n========== REPORTE DE REGISTRO ==========\n")
                        print(f"La categoria es: {Category}")
                        print(f"El tipo de Vehiculo es: {vehiculo}")
                        print(f"El monto base en soles es: {montoBaseSoles:.2F}")
                        print(F"El monto de impuestos en soles es: {(montoBaseSoles * dsto):.2f}")
                        print(f"El monto total a pagar en soles es: {montoTotalSoles:.2f}")

                        AcumuladoPagarSoles = AcumuladoPagarSoles + montoTotalSoles

                        break

                    case 5:
                        contadorAcciones = contadorAcciones + 1  
                        contadorAccionesE = contadorAccionesE + 1

                        Category = "E"
                        vehiculo = "Trailer"
                        dsto = 0.12

                        montoImpuesto = montoBase * dsto
                        montoTotal = montoBase + montoImpuesto
                        montoBaseSoles = montoBase * tipoCambio
                        montoTotalSoles = montoTotal * tipoCambio           

                        print("\n========== REPORTE DE REGISTRO ==========\n")
                        print(f"La categoria es: {Category}")
                        print(f"El tipo de Vehiculo es: {vehiculo}")
                        print(f"El monto base en soles es: {montoBaseSoles:.2F}")
                        print(F"El monto de impuestos en soles es: {(montoBaseSoles * dsto):.2f}")
                        print(f"El monto total a pagar en soles es: {montoTotalSoles:.2f}")       

                        AcumuladoPagarSoles = AcumuladoPagarSoles + montoTotalSoles

                        break     
        
        case 2:
            print("\n========== REPORTE POR TOTAL ==========\n")
            print(f"La acciones realizadas es: {contadorAcciones}")
            print(f"El acumulado de calculos C: {contadorAccionesC}")
            print(f"El monto total a pagar en soles es: {AcumuladoPagarSoles:.2f}")
            print(f"El monto total a pagar en soles categoria B es: {AcumuladoPagarSolesB:.2f}")
            print(f"Acumulado de los montos totales sea mayor a 5000 es: {AcumuladoMontoTotal5K}")
        
        case 3:
            print("Saliendo del programa...")

            break