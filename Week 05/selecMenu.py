montoSaldo = 0

print("\n========== MENU CAJERO ==========")
print("1. Depositar")
print("2. Retirar")
print("3. Ver Saldo")
print("4. Salir")

optionMenu = int(input("Ingrese la opción: "))

if (optionMenu >= 1 and optionMenu <= 4):

    match optionMenu:
        case 1:
            montoDepos = float(input("Ingrese el monto a Depositar: "))

            if montoDepos > 0:
                montoSaldo = montoSaldo + montoDepos
            else:
                print("[ERROR] El monto a depositar debe ser mayor a 0")

        case 2:
            montoRetir = float(input("Ingrese el monto a retirar: "))

            if montoRetir > 0:
                if montoRetir <= montoSaldo:
                    montoSaldo = montoSaldo - montoRetir
                else:
                    print("----- SALDO INSUICIENTE -----")
            else:
                print("[ERROR] El monto a retirar debe ser mayor a 0")
        
        case 3:
            print(f"Su saldo actual es de: {montoSaldo}")
        
        case 4:
            print("Gracias---- Vuelva Pronto")
else:
    print("[ERROR] Ingrese un número valido")
