global contador
contador = 0

def mayMen(datoIngresado, contador):
    global may
    global men

    if (contador == 1):
        may = datoIngresado
        men = datoIngresado
    elif (datoIngresado > may):
        may = datoIngresado
    else:
        if (datoIngresado < men):
            men = datoIngresado

def ejecutar():
    global contador

    while True:
        print(50 * "=")

        datoIngresado = eval(input("Ingrese un dato: "))
        contador = contador + 1

        mayMen(datoIngresado, contador)

        while True:
            rpta = input("Desea ingresar otro dato? (S/N): ")
            rptaMayusc = rpta.upper()

            if (rptaMayusc != "S" and rptaMayusc != "N"):
                print("[ERROR] Vuelva a ingresar, opcion no valida")
            else:
                break

        if (rptaMayusc != "S"):
            print(f"El dato mayor es: {may}")
            print(f"El dato menor es: {men}")
            break

ejecutar()