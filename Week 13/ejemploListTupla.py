global MiLista
global MiTupla

MiLista = []
MiTupla = ()


def RegistrarTupla():
    global MiTupla
    MiTupla = ('Papel', 'Cuaderno', 'Lapicero', 'Lapiz')
    print("-> Tupla de productos registrada.")


def RegistrarLista():
    global MiLista
    # La tupla tiene 4 productos, así que usamos 4 precios
    MiLista = [5.00, 8.50, 3.00, 2.50]
    print("-> Lista de precios registrada.")


def MostrarProductoPrecio():
    print("\n--- Mostrando Productos y Precios ---")

    # Primero nos aseguramos de que los datos estén registrados
    RegistrarLista()
    RegistrarTupla()

    Reporte = list(zip(MiTupla, MiLista))

    print("\nReporte (Producto, Precio):")
    for producto, precio in Reporte:
        print(f"- Producto: {producto}, Precio: S/ {precio:.2f}")


def menu():
    print("\n======== MENÚ GUÍA SEMANA 13 ========")
    print("1. Mostrar Reporte Productos y Precios")
    print("2. Salir")

    while True:
        op = int(input("Ingrese una opción: "))
        if (op < 1 or op > 2):
            print("[ERROR] Opción no válida. Ingrese 1 o 2.")
        else:
            return op


def ejecutar():
    while True:
        opcion = menu()
        if opcion == 1:
            MostrarProductoPrecio()
        elif opcion == 2:
            print("Saliendo del programa...")
            break


# --- Iniciar el programa ---
ejecutar()