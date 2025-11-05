def leerDatoF():
    dato = float(input(""))
    return dato

def DeterminaPorcentaje(sueldo):
    if sueldo >= 5001:
        porcentaje = 0.10
    elif sueldo >= 3501:
        porcentaje = 0.15
    elif sueldo >= 2001:
        porcentaje = 0.20
    else:
        porcentaje = 0.25
    return porcentaje

def CalculaSueldoTotal(sueldo_base):
    porcentaje = DeterminaPorcentaje(sueldo_base)
    monto_aumento = sueldo_base * porcentaje
    sueldo_total = sueldo_base + monto_aumento

    print("\n======== REPORTE DE SUELDO ========")
    print(f"Sueldo Base \t\t: S/. {sueldo_base:,.2f}")
    print(f"Porcentaje de Aumento \t: {int(porcentaje * 100)}%")
    print(f"Monto de Aumento \t: S/. {monto_aumento:,.2f}")
    print(f"Sueldo Total \t\t: S/. {sueldo_total:,.2f}")
    print("=" * 35)

def procesarCalculo():
    while True:
        sueldo = leerDatoF("Ingrese el sueldo base del trabajador: ")
        if sueldo > 0:
            CalculaSueldoTotal(sueldo)
            break
        else:
            print("[ERROR] El sueldo debe ser mayor a 0. Vuelva a ingresar.")

def menu():
    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1. Procesar Cálculo de Sueldo")
        print("2. Salir")

        opcionMenu = int(input("Ingrese una opción del menú: "))

        match opcionMenu:
            case 1:
                procesarCalculo()
            case 2:
                print("Saliendo del programa...")
                break

def ejecutar():
    menu()

ejecutar()