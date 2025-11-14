print("===== datos para el horario =====")

def IngresaDatosTupla():
    tuplaHorario = () # crear una vacia
    ListaHorario = list(tuplaHorario)
    for i in range(3):
        valor = input("Ingrese valor: ")
        ListaHorario.append(valor)
    tuplaHorario = tuple(ListaHorario)
    return tuplaHorario

def MostrarDatosTupla(miTupla):
    if miTupla:
        print("Los elementos de la tupla son:")
        for elemento in miTupla:
            print(elemento, ", ", end="")
    else:
        print("La tupla está vacia o contiene elementos no validos.")

miTupla = IngresaDatosTupla()
MostrarDatosTupla(miTupla)