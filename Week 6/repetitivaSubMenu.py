montoSaldo = 0

while True:
    print("\n======== MENÚ PRinicpal ==========")
    print("1. Procesar")
    print("2. Salir")

    while True:
        opcionMenu = int(input("Ingrese opcion de menú: "))

        if (opcionMenu<1 or opcionMenu>2):
            print("ERROR. Vuelva a ingresar 1 ó 2")
        else:
            break
    
    match opcionMenu:
        case 1:
            while True:
                print("\n======== SUB MENÚ CAJERO ==========")
                print("1. Depositar")
                print("2. Retirar")
                print("3. Ver Saldo")
                print("4. Volver")

                while True:
                    opcionSubMenu = int(input("Ingrese opcion de menú: "))

                    if (opcionSubMenu < 1 or opcionSubMenu > 4):
                        print("[ERROR] Vuelva a ingresar 1 ó 2 ó 3 ó 4")
                    else:
                        break
                
                match opcionSubMenu:
                    case 1:
                        while True:
                            montoDepos = float(input("Ingrese Monto a Depositar: "))

                            if (montoDepos <= 0):
                                print("[ERROR] Vuelva a ingresar, Monto deposito debe ser mayor a 0")
                            else:
                                break

                        montoSaldo = montoSaldo + montoDepos
                    
                    case 2:
                        while True:
                            montoRetir = float(input("Ingrese Monto a Retirar: "))

                            if (montoRetir <= 0):
                                print("[ERROR] Vuelva a ingresar, Monto retiro debe ser mayor a 0")
                            else:
                                break
                        
                        if montoRetir <= montoSaldo:
                            montoSaldo = montoSaldo - montoRetir
                        else:
                            print("---------- Saldo Insuficiente. -------------")
                    
                    case 3:
                        print(f"Su saldo actual es: {montoSaldo}")

                    case 4:
                        while True:
                            rptaS = input("Seguro que quiere Volver? (S o s o N o n): ")
                            rptaSMayusc = rptaS.upper()

                            if (rptaSMayusc != "S" and rptaSMayusc!="N"):
                                print("[ERROR] Vuelva a ingresar S o s o N o n")
                            else:
                                break

                        if rptaSMayusc == "S":
                            print("Estas volviendo al Menú Principal")

                            break
        
        case 2:
            while True:
                rptaMp = input("Seguro que quiere Salir? (S ó s ó N ó n): ")
                rptaMpMayusc = rptaMp.upper()

                if (rptaMpMayusc != "S" and rptaMpMayusc != "N"):
                    print("[ERROR] Vuelva a ingresar S ó s ó N ó n")
                else:
                    break

            if rptaMpMayusc == "S":
                print("[Gracias] Vuelva pronto..!")
                break