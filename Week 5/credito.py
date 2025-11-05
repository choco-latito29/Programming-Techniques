print("\n========== NIVEL DE AVANCE ACADÉMICO ==========\n")

creditos = int(input("Ingrese la cantidad de créditos acumulados: "))

if (creditos >= 0):

    if (creditos <= 160):

        año_academico = ""

        if creditos < 32:
            año_academico = "Primer año"
        elif creditos <= 63:
            año_academico = "Segundo año"
        elif creditos <= 95:
            año_academico = "Tercer año"
        elif creditos <= 127:
            año_academico = "Cuarto año"
        else:
            año_academico = "Quinto año"
        
        print(f"Año académico: {año_academico}")

    else:
        print("[Error] La cantidad de créditos no puede ser mayor a 160.")
else:
    print("[Error] La cantidad de créditos debe ser un número positivo.")