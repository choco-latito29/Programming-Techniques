print("\n========== INGRESO DE DATOS DE BARCO ==========")

letra = input("Ingrese un número para una vocal: ")
letraMayusc = letra.upper()

if (letraMayusc == "B" or letraMayusc == "F" or letraMayusc == "C"):

    match letraMayusc:
        case "B":
            print("Es un buque")
        
        case "F":
            print("Es la vocal fragata")
        
        case "C":
            print("Es la vocal crucero")
else:
    print("ERROR, no es letra para barco")