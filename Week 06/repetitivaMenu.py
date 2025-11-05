montoSaldo = 0

while True:

    print("\n========== MENU CAJERO ==========\n")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver Saldo")
    print("4. Salir")

    while True:
        opcionMenu = int(input("Ingrese la opción del menú: "))
        if (opcionMenu < 1 or opcionMenu > 4):
            print("[ERROR] Vuelva a Ingresar....")
        else:
            break
    
    match opcionMenu:

        case 1:
            while True:
                montoDepos = float(input("Ingrese monto a depositar: "))
                if (montoDepos <= 0):
                    print("[ERROR] Vuelva a ingresar el monto")
                else:
                    montoSaldo = montoSaldo + montoDepos
                    break
        
        case 2:
            while True:
                montoRetir = float(input("Ingrese el monto a retirar: "))
                if (montoRetir <= 0):
                    print("[ERROR] Vuelva a ingresar el monto")
                else:
                    if montoRetir <= montoSaldo:
                        montoSaldo = montoSaldo - montoRetir
                    else:
                        print("------------ Saldo Insuficiente ------------")
                    break

        case 3:
            print(f"Su saldo actual es: {montoSaldo}")

        case 4:
            print("[Gracias] Vuelva pronto...")
            break
