print("=" * 50)

def hanoi(n, org, aux, des):
    movimientos = 0
    if (n == 1):
        print(org, " -> ", des)
        movimientos = 1
    else:
        movimientos += hanoi(n - 1, org, des, aux)
        print(org, " -> ", des)
        movimientos += 1
        movimientos += hanoi(n - 1, aux, org, des)
    return movimientos

def ejecutar():
    while True:
            n = int(input("Ingrese la cantidad de discos: "))

            if (n <= 0):
                print("[ERROR] Vuelva a ingresar...")
            else:
                break
    
    print("\nIniciando movimientos:\n")
    
    total_movimientos = hanoi(n, "A", "B", "C")
    
    print("\n--- Proceso Completado ---")
    print(f"Total de movimientos realizados: {total_movimientos}")

ejecutar()