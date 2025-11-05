while True:

    print("\n=========== MENU OPCIONES =============\n")
    print("1. Vender")
    print("2. Salir")

    while True:
        op = int(input(("Ingrese opcion de menú: ")))

        if (op < 1 or op > 2):
            print("ERROR. Vuelva a ingresar")
        else:
            break

    match op:
        case 1:
            nombreProd = input("Ingrese Nombre de Producto: ")

            while True:
                precioProd = float(input("Ingrese Precio de Producto: "))

                if (precioProd <= 0):
                    print("[ERROR] Vuelva a ingresar")
                else:
                    break

            while True:
                cantidadProd = int(input("Ingrese Cantidad de Producto: "))

                if (cantidadProd <= 0):
                    print("ERROR. Vuelva a ingresar")
                else:
                    break

            while True:
                porentajecDcto = float(input("Ingrese Porcentaje Descuento: "))

                if (porentajecDcto <= 0):
                    print("ERROR. Vuelva a ingresar")
                else:
                    break

            while True:
                genero = (input("Ingrese Genero: "))
                generoMayus = genero.upper()

                if (generoMayus != 'F' and generoMayus != 'M'):
                    print("[ERROR] Vuelva a ingresar")
                else:
                    break

            match generoMayus:
                case 'M':
                    bono = 0.18

                    if (cantidadProd <= 10):
                        dcto = 0.2
                    else:
                        dcto = 0.5

                case 'F':
                    bono = 0.25

                    if (cantidadProd <= 10):
                        dcto = 0.3
                    else:
                        dcto = 0.4

            montoBruto = precioProd * cantidadProd
            montoBono = montoBruto * bono
            montoDcto = montoBruto * porentajecDcto
            montoPago = montoBruto - montoDcto + montoBono

            print("\n=========== REPORTE =============\n")
            print(f"El Monto Bruto es: {montoBruto}")
            print(f"EL Monto bono es: {montoBono}")
            print(f"El Monto Descuento es: {montoDcto}")
            print(f"El Monto a Pagar es: {montoPago}")

        case 2:
            print("Gracias Vuelva Pronto..!")
            
            break
