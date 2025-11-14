print("======= Datos para el curso =======")

ListaCurso = []

max_rang = int(input("Ingrese el maximo rango: "))

def IngresarDatosLista():
    for i in range(max_rang):
        valor = input("Ingrese el valor: ")
        ListaCurso.append(valor)

def MostrarDatosLista(ListaCurso):
    if ListaCurso:
        print("Los elementos de la lista son: ")
        for elemento in ListaCurso:
            print(elemento, " ", end=" ")
    else:
        print("La lista esta vacia o contiene elementos no validos")

IngresarDatosLista()
MostrarDatosLista(ListaCurso)