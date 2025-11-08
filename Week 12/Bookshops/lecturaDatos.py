def leerFloatPositivo(mensaje):
    while True:
        valor = float(input(mensaje))

        if (valor <= 0):
            print("[ERROR] El valor debe ser positivo.")
        else:
            return valor
        
def leerOpcionMenu(mensaje, min_op, max_op):
    while True:
        op = int(input(mensaje))

        if (op < min_op or op > max_op):
            print(f"[ERROR] Opción no válida. Ingrese una opción entre {min_op} y {max_op}.")
        else:
            return op
        
def leerCategoria(mensaje):
    while True:
        cat = input(mensaje).upper()

        if (cat in ['A', 'B', 'C', 'D', 'E']):
            return cat
        else:
            print("[ERROR] Categoría no válida. Ingrese una categoría entre A y E.")