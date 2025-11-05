print("\n========== INGRESO DE DATOS =========\n")

while True:
    num = eval(input("Ingrese el número para una vocal: "))

    if (num < 1 or num > 5):
        print("[ERROR] vuelva a ingresar..")
    else:
        break

match num:
    case 1:
        print("Es la vocal a")
    
    case 2:
        print("Es la vocal e")

    case 3:
        print("Es la vocal i")
    
    case 4:
        print("Es la vocal o")
    
    case 5:
        print("Es la vocal u")