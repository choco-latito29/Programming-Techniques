def ingresarDatosLista():
    ListaCurso = []

    rango = int(input("Ingrese el rango de la lista: "))
    for i in range(rango):
        valor = input(f"Ingrese el valor {i + 1}/{rango}: ")
        ListaCurso.append(valor)

    print("¡Lista creada exitosamente!")
    return ListaCurso


def mostrarDatosLista(miLista):
    if miLista:
        print("\n--- Mostrando Lista ---")
        print("Los elementos de la lista son: ")
        for elemento in miLista:
            print(elemento, ", ", end="")
        print()
    else:
        print("\n[AVISO] La lista está vacia. Use la opción 1 para ingresar datos.")


def IngresaDatosTupla():
    ListaHorario = []

    rango = int(input("Ingrese el rango de la tupla: "))

    for i in range(rango):
        valor = input(f"Ingrese valor {i + 1}/{rango}: ")
        ListaHorario.append(valor)
    tuplaHorario = tuple(ListaHorario)
    print("¡Tupla creada exitosamente!")
    return tuplaHorario


def MostrarDatosTupla(miTupla):
    if miTupla:
        print("\n--- Mostrando Tupla ---")
        print("Los elementos de la tupla son:")
        for elemento in miTupla:
            print(elemento, ", ", end="")
        print()
    else:
        print("\n[AVISO] La tupla está vacia. Use la opción 3 para ingresar datos.")


def menu():
    print("\n======== MENÚ LISTAS Y TUPLAS ========")
    print("1. Ingresar datos a la Lista")
    print("2. Mostrar datos de la Lista")
    print("3. Ingresar datos a la Tupla")
    print("4. Mostrar datos de la Tupla")
    print("5. Salir")

    while True:
        op = int(input("Ingrese una opción: "))

        if (op < 1 or op > 5):
            print("[ERROR] Opción no válida. Ingrese de 1 a 5.")
        else:
            return op


def ejecutar():
    miListaPrincipal = []
    miTuplaPrincipal = ()

    while True:
        opcion = menu()

        match opcion:
            case 1:
                miListaPrincipal = ingresarDatosLista()
            case 2:
                mostrarDatosLista(miListaPrincipal)
            case 3:
                miTuplaPrincipal = IngresaDatosTupla()
            case 4:
                MostrarDatosTupla(miTuplaPrincipal)
            case 5:
                print("Saliendo del programa...")
                break


ejecutar()