print("===== datos para el horario =====")

def IngresaDatosTupla():
    tuplaHorario = () # crear una vacia

    for i in range(3):
        valor = input("Ingrese valor: ")

        # guardar la nueva tupla
        tuplaHorario = tuplaHorario + (valor,)
    
    return tuplaHorario # devolver la tupla completa

print(IngresaDatosTupla())