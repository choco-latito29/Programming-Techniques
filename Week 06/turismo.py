while True:

    print("\n========== MENU PRINCIPAL ==========")
    print("1. Procesar")
    print("2. Salir")

    while True:
        opcionMenu = int(input("Ingrese opcion de menú: "))

        if (opcionMenu < 1 or opcionMenu > 2):
            print("ERROR. Vuelva a ingresar 1 o 2")
        else:
            break

    match opcionMenu:

        case 1:
            while True:

                print("\n------ SUBMENU DESTINOS TURISTICOS ------")
                print("1. Punta Cana")
                print("2. San Andrés")
                print("3. Cancún")
                print("4. Volver")

                while True:
                    opcionSubMenu = int(input("Ingrese opcion de menú: "))

                    if (opcionSubMenu < 1 or opcionSubMenu > 4):
                        print("[ERROR] Vuelva a ingresar 1, 2, 3 o 4")
                    else:
                        break

                match opcionSubMenu:
                    case 1:
                        while True:
                            cantidadPersonas = int(input("Ingrese la cantidad de personas: "))

                            if (cantidadPersonas <= 0):
                                print("[ERROR] La cantidad debe ser mayor a cero.")
                            else:
                                break

                        while True:
                            tipoCambio = float(input("Ingrese el tipo de cambio del día: "))

                            if (tipoCambio <= 0):
                                print("[ERROR] El tipo de cambio debe ser un valor positivo.")
                            else:
                                break
                        
                        precio_usd = 780
                        porcentaje_dcto = 0.035

                        subtotal_usd = precio_usd * cantidadPersonas
                        monto_dcto_usd = 0

                        if (cantidadPersonas > 4):
                            monto_dcto_usd = subtotal_usd * porcentaje_dcto

                        total_usd = subtotal_usd - monto_dcto_usd
                        total_soles = total_usd * tipoCambio

                        print(f"El total a pagar es: {total_soles} soles")

                    case 2:
                        while True:
                            cantidadPersonas = int(input("Ingrese la cantidad de personas: "))

                            if (cantidadPersonas <= 0):
                                print("[ERROR] La cantidad debe ser mayor a cero.")
                            else:
                                break

                        while True:
                            tipoCambio = float(input("Ingrese el tipo de cambio del día: "))

                            if (tipoCambio <= 0):
                                print("[ERROR] El tipo de cambio debe ser un valor positivo.")
                            else:
                                break
                        
                        precio_usd = 1350
                        porcentaje_dcto = 0.04
                        subtotal_usd = precio_usd * cantidadPersonas
                        monto_dcto_usd = 0

                        if (cantidadPersonas > 4):
                            monto_dcto_usd = subtotal_usd * porcentaje_dcto

                        total_usd = subtotal_usd - monto_dcto_usd
                        total_soles = total_usd * tipoCambio

                        print(f"El total a pagar es: {total_soles} soles")

                    case 3:
                        while True:
                            cantidadPersonas = int(input("Ingrese la cantidad de personas: "))

                            if (cantidadPersonas <= 0):
                                print("[ERROR] La cantidad debe ser mayor a cero.")
                            else:
                                break

                        while True:
                            tipoCambio = float(input("Ingrese el tipo de cambio del día: "))

                            if (tipoCambio <= 0):
                                print("[ERROR] El tipo de cambio debe ser un valor positivo.")
                            else:
                                break

                        precio_usd = 2550
                        porcentaje_dcto = 0.045
                        subtotal_usd = precio_usd * cantidadPersonas
                        monto_dcto_usd = 0

                        if (cantidadPersonas > 4):
                            monto_dcto_usd = subtotal_usd * porcentaje_dcto

                        total_usd = subtotal_usd - monto_dcto_usd
                        total_soles = total_usd * tipoCambio

                        print(f"El total a pagar es: {total_soles} soles")
                    
                    case 4:
                        while True:
                            rptaS = input("¿Seguro que quiere Volver? (S o s o N o n): ")
                            rptaSMayusc = rptaS.upper()

                            if (rptaSMayusc != "S" and rptaSMayusc != "N"):
                                print("[ERROR] Vuelva a ingresar S o s o N o n")
                            else:
                                break

                        if rptaSMayusc == "S":
                            print("Estas volviendo al Menú Principal")

                            break
        
        case 2:
            while True:
                rptaMp = input("¿Seguro que quiere Salir? (S o s o N o n): ")
                rptaMpMayusc = rptaMp.upper()

                if (rptaMpMayusc != "S" and rptaMpMayusc != "N"):
                    print("[ERROR] Vuelva a ingresar S o s o N o n")
                else:
                    break

            if rptaMpMayusc == "S":
                print("[Gracias] Vuelva pronto..!")
                
                break