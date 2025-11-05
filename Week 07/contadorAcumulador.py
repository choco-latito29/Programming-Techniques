contadorCurso = 0
acumuladorCredito = 0

while True:

    print("\n========== MENU DE OPCIONES ==========\n")
    print("1. Procesar")
    print("2. Reportar")
    print("3. Salir")

    while True:
        op = int(input("Ingrese una opción: "))

        if (op < 1 or op > 3):
            print("[ERROR] Vuelve a ingresar")
        else:
            break

    match op:
        case 1:
            nombreCurso = input("Ingrese el nombre del curso: ")

            contadorCurso = contadorCurso + 1

            while  True:
                creditoCurso = int(input(f"Ingrese el créditos (1 a 5) de Cursos: "))

                if (creditoCurso <= 0 or creditoCurso > 6):
                    print("[ERROR] El crédito no puede ser negativo. Intente de nuevo.")
                else:
                    break
            
            acumuladorCredito = acumuladorCredito + creditoCurso
        
        case 2:
            print("\n========== REPORTE POR TOTAL ==========\n")
            print(f"La cantidad de cursos es: {contadorCurso}")
            print(f"El acumulado de créditos es: {acumuladorCredito}")
        
        case 3:
            print("Saliendo del programa...")
            break