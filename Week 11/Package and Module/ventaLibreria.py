import Bookshops.utilitarios as util
import Bookshops.operacionesAritmeticas as calculadora

global montMasc, contFem, contTotalClien, cantMascMayMil, acumTotalVentas, acumVentasFem
global montoPago, montoBruto, montoBono, montoDcto

contMasc = 0
contFem = 0
contTotalClien = 0
cantMascMayMil = 0
acumTotalVentas = 0
acumVentasFem = 0

def reportar():
    print("\n========== REPORTE POR TOTAL ==========\n")
    print(f"La cantidad total de clientes es: {contTotalClien}")
    print(f"La cantidad de clientes Femenino es: {contFem}")
    print(f"La cantidad de clientes Masculino es: {contMasc}")
    print(f"La cantidad de clientes Masculino, acumulado >= 1000 es: {cantMascMayMil}")
    print(f"El acumulado total de ventas es: {acumTotalVentas}")
    print(f"El acumulado total de ventas de clientes Femenino es: {acumVentasFem}")

def procesar():
    global contMasc, contFem, contTotalClien, cantMascMayMil, acumTotalVentas, acumVentasFem
    global montoPago, montoBruto, montoBono, montoDcto

    nombreProd = input("Ingrese el nombre del producto: ")

    while True:
        precioProd = float(input("Ingrese el precio del producto: "))

        if (precioProd <= 0):
            print("[ERROR] Vuelva a ingresar")
        else:
            break

    while True:
        cantidadProd = int(input("Ingrese la cantidad del producto: "))

        if (cantidadProd <= 0):
            print("[ERROR] Vuelva a ingresar")
        else:
            break

    while True:
        porentajecDcto = float(input("Ingrese el porcentaje de descuento: "))

        if (porentajecDcto <= 0):
            print("[ERROR] Vuelva a ingresar")
        else:
            break

    while True:
        genero = (input("Ingrese el genero: "))
        generoMayus = genero.upper()

        if (generoMayus != 'F' and generoMayus != 'M'):
            print("[ERROR] Vuelva a ingresar")
        else:
            break

    match generoMayus:
        case 'M':
            contMasc = contMasc + 1

            bono = 0.18

            if (cantidadProd <= 10):
                dcto = 0.2
            else:
                dcto = 0.5

        case 'F':
            contFem = contFem + 1

            bono = 0.25

            if (cantidadProd <= 10):
                dcto = 0.3
            else:
                dcto = 0.4

    montoBruto = calculadora.multiplicar(precioProd, cantidadProd)
    montoBono = calculadora.multiplicar(montoBruto, bono)
    montoDcto = calculadora.multiplicar(montoBruto, porentajecDcto)
    montoPago = calculadora.sumar(calculadora.restar(montoBruto, montoDcto), montoBono)

    contTotalClien = contTotalClien + 1
    acumTotalVentas = calculadora.sumar(acumTotalVentas, montoPago)

    if (generoMayus == 'F'):
        acumVentasFem = acumVentasFem + montoPago

    if (generoMayus == 'M' and acumTotalVentas >= 1000):
        cantMascMayMil = cantMascMayMil + 1

    print("\n========== REPORTE POR CLIENTE ==========\n")
    print(f"El monto bruto es: {montoBruto}")
    print(f"El monto del bono es: {montoBono}")
    print(f"El monto del descuento es: {montoDcto}")
    print(f"El monto a pagar es: {montoPago}")

def menu():
    print("\n========== MENU DE OPCIONES ==========\n")
    print("1. Procesar")
    print("2. Reportar")
    print("3. Salir")

    while True:
        op = int(input("Ingrese una opcion del menu: "))

        if (op < 1 or op > 3):
            print("[ERROR] Vuelva a ingresar")
        else:
            break
    
    match op:
        case 1:
            procesar()

        case 2:
            reportar()

        case 3:
            while True:
                rpta = input("Desea salir del sistema? (S/N): ")
                rptaMayus = rpta.upper()

                if (rptaMayus != 'S' and rptaMayus != 'N'):
                    print("[ERROR] Vuelva a ingresar")
                else:
                    break

            if (rptaMayus == 'S'):
                util.salir()
            else:
                menu()

    return op

def ejecutar():
    while True:
        opcion = menu()

        if (opcion == 3):
            break

ejecutar()