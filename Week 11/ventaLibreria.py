import Bookshops.utilitarios as util
import Bookshops.operacionesAritmeticas as calculadora
import Bookshops.lecturaDatos as lector

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

    nombreProd = input("Ingrese el nombre del producto: ")
    precioProd = lector.leerFloatPositivo("Ingrese el precio del producto: ")
    cantidadProd = lector.leerIntPositivo("Ingrese la cantidad del producto: ")
    porentajecDcto = lector.leerFloatPositivo("Ingrese el porcentaje de descuento: ")
    generoMayus = lector.leerGenero("Ingrese el genero (F/M): ")

    match generoMayus:
        case 'M':
            contMasc = contMasc + 1

            bono = 0.18
            dcto = 0.2 

            if (cantidadProd <= 10):
                dcto = 0.2
            else:
                dcto = 0.5
        case 'F':
            contFem = contFem + 1
            bono = 0.25
            dcto = 0.3

            if (cantidadProd <= 10):
                dcto = 0.3
            else:
                dcto = 0.4

    montoBruto = calculadora.multiplicar(precioProd, cantidadProd)
    montoBono = calculadora.multiplicar(montoBruto, bono)
    montoDcto = calculadora.multiplicar(montoBruto, porentajecDcto / 100)
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

    op = lector.leerOpcionMenu("Ingrese una opcion del menu: ", 1, 3)

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
                op = 0 

    return op

def ejecutar():
    while True:
        opcion = menu()

        if (opcion == 3):
            break

ejecutar()