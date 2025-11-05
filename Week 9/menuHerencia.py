def leerDatoE():
    dato = int(input(""))
    return dato

def leerDatoF():
    dato = float(input(""))
    return dato

def reparticion():
    while True:
        print("Ingrese Monto de Herencia: ")

        montoHerencia = leerDatoF()

        if (montoHerencia <= 0):
            print("[ERROR] Vuelva a ingresar, monto de herencia debe ser mayor a 0")
        else:
            break

    while True:
        print("Ingrese cantidad de hijos: ")

        cantidadHijos = leerDatoE()

        if (cantidadHijos <= 0):
            print("[ERROR] Vuelva a ingresar, cantidad de hijos debe ser mayor a 0")
        else:
            break

    if (cantidadHijos <= 3):
        reparto = montoHerencia / cantidadHijos

        print(f"Para cada hijo se reparte: {reparto}")
    elif (cantidadHijos >= 4):
        repartHijoMayor = montoHerencia / 2

        reparto = repartHijoMayor / (cantidadHijos - 1)

        print(f"Para el hijo mayor se reparte: {repartHijoMayor}")
        print(f"Para los demas hijos se reparte: {reparto}")

def menu():
    while True:
        print("\n========== MENU PRINCIPAL ==========\n")
        print("1. Procesar")
        print("2. Salir")

        while True:
            opcionMenu = int(input("Ingrese una opcion del menu: "))

            if (opcionMenu < 1 or opcionMenu > 2):
                print("[ERROR] Vuelva a ingresar, opcion no valida")
            else:
                break

        match opcionMenu:
            case 1:
                reparticion()
                
            case 2:
                while True:
                    rptMp = input("Seguro que quiere dalir? (S o s o N o n): ")
                    rptMpMayusc = rptMp.upper()

                    if (rptMpMayusc != "S" and rptMpMayusc != "N"):
                        print("[ERROR] Vuelva a ingresar, opcion no valida")
                    else:
                        break

                if (rptMpMayusc == "S"):
                    print("Saliendo del programa...")
                    break

def ejecutar():
    menu()

ejecutar()