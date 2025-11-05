global contMasc, contFem, contTotalClien, cantMascMayMil, acumTotalVentas, acumVentasFem
contMasc = 0
contFem = 0
contTotalClien = 0
cantMascMayMil = 0
acumTotalVentas = 0
acumVentasFem = 0

def salir():
    print("Gracias Vuelva Pronto..!")

def reportar():
    print("\n======== REPORTE POR TOTAL ==========\n")
    print(f"La cantidad Total de Clientes es: {contTotalClien}")
    print(f"La cantidad de Clientes Femenino es: {contFem}" )
    print(f"La cantidad de Clientes Masculino es: {contMasc}")
    print(f"La cantidad de Clientes Masculino, acumulado > 1000 es: {cantMascMayMil}")
    print(f"El acumulado Total de Ventas es: {acumTotalVentas}")
    print(f"El acumulado Total de Ventas de Cliente Femenino es: {acumVentasFem}" )

def procesar():
    global contMasc, contFem, contTotalClien, cantMascMayMil, acumTotalVentas, acumVentasFem

    nombreProd = input("Ingrese Nombre de Producto: ")

    while True:
        precioProd = float(input("Ingrese Precio de Producto: "))

        if (precioProd <= 0):
            print("[ERROR]. Vuelva a ingresar")
        else:
            break

    while True:
        cantidadProd = int(input("Ingrese Cantidad de Producto: "))

        if (cantidadProd <= 0):
            print("[ERROR]. Vuelva a ingresar")
        else:
            break
    
    while True:
        porentajecDcto = float(input("Ingrese Porcentaje Descuento: "))

        if (porentajecDcto <= 0):
            print("[ERROR]. Vuelva a ingresar")
        else:
            break

    while True:
        genero = (input("Ingrese Genero: "))
        generoMayus = genero.upper()

        if (generoMayus != 'F' and generoMayus != 'M'):
            print("[ERROR]. Vuelva a ingresar")
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

    montoBruto = precioProd * cantidadProd
    montoBono = montoBruto * bono
    montoDcto = montoBruto * porentajecDcto
    montoPago = montoBruto - montoDcto + montoBono

    contTotalClien = contTotalClien + 1
    acumTotalVentas = acumTotalVentas + montoPago

    if (generoMayus == 'F'):
        acumVentasFem = acumVentasFem + montoPago

    if (generoMayus == 'M' and acumTotalVentas >= 1000):
        cantMascMayMil = cantMascMayMil + 1

    print("\n=========== REPORTE POR CLIENTE ===========\n")
    print(f"El Monto Bruto es: {montoBruto}" )
    print(f"EL Monto bono es: {montoBono}")
    print(f"EL Monto Descuento es: {montoDcto}", )
    print(f"EL Monto a Pagar es: {montoPago}")

def menu():
    print("\n======== MENU OPCIONES ==========\n")
    print("1. Procesar")
    print("2. Reportar")
    print("3. Salir")

    while True:
        op = int(input("Ingrese opcion de menú: "))

        if (op < 1 or op > 3):
            print("[ERROR]. Vuelva a ingresar")
        else:
            break
    
    match op:
        case 1: 
            procesar()
        
        case 2: 
            reportar()

        case 3:
            while True:
                rpta = input("Desea salir del programa? (S/N):")
                rptMayusc = rpta.upper()

                if (rptMayusc != 'S' and rptMayusc != 'N'):
                    print("[ERROR]. Vuelva a ingresar")
                else:
                    break
            
            if (rptMayusc == 'S'):
                salir()
            else:
                menu()
    
    return op;

def ejecutor():
    while True:
        opcion = menu() 

        if (opcion == 3):
            break

ejecutor()