def leerFloatPositivo(mensaje):
    while True:
        valor = float(input(mensaje))
        
        if (valor <= 0):
            print("[ERROR] Vuelva a ingresar.")
        else:
            return valor

def leerIntPositivo(mensaje):
    while True:
        valor = int(input(mensaje))

        if (valor <= 0):
            print("[ERROR] Vuelva a ingresar.")
        else:
           return valor

def leerGenero(mensaje):
    while True:
        generoMayus = input(mensaje).upper()

        if (generoMayus != 'F' and generoMayus != 'M'):
            print("[ERROR] Vuelva a ingresar (F/M).")
        else:
            return generoMayus

def leerOpcionMenu(mensaje, min_op, max_op):
     while True:
        op = int(input(mensaje))
        if (op < min_op or op > max_op):
            print(f"[ERROR] Vuelva a ingresar (Opción de {min_op} a {max_op}).")
        else:
            return op