print("\n========== INGRESO DE DATOS ==========")

num = eval(input("Ingrese un número para una vocal: "))

if (num >= 1 and num <= 5):

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
else:
    print("ERROR, debe ingresar del 1 al 5")