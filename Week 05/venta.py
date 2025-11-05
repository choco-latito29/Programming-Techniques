print("\n ========== INGRESO DE DATOS ==========\n")

nombreProduct = input("Ingrese el nombre del producto: ")
precioProduct = float(input("Ingrese el precio del producto: "))

if (precioProduct > 0):
    cantProduct = int(input("Ingrese cantidad de producto: "))

    if (cantProduct > 0):
        porcentDescuento = float(input("Ingrese el porcentaje de descuento: "))

        if (porcentDescuento > 0):
            genero = (input("Ingrese el genero: "))
            generoMayusc = genero.upper()

            if (generoMayusc == "F" or generoMayusc == "M"):

                match generoMayusc:
                    case "M":
                        bono = 0.18

                        if (cantProduct <= 10):
                            dcto = 0.2
                        else:
                            dcto = 0.5

                    case "F":
                        bono = 0.25
                        
                        if (cantProduct <= 10):
                            dcto = 0.3
                        else:
                            dcto = 0.4
                
                montoBruto = precioProduct * cantProduct
                montoBono = montoBruto * bono
                montoDcto = (montoBruto * porcentDescuento) / 100
                montoPago = montoBruto - montoDcto + montoBono

                print("\n========== REPORTE ==========\n")
                print(f"El monto bruto es: {montoBruto}")
                print(f"El monto bono es: {montoBono}")
                print(f"El monto descuento es: {montoDcto}")
                print("---------------------------------------")
                print(f"El monto a pagar es: {montoPago}")

            else:
                print("Error de genero")
        else:
            print("Error de porcentaje")
    else:
        print("Error de cantidad")
else:
    print("Error de precio")