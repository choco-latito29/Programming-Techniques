a = 1 # Primer valor de la serie
b = 1 # Segundo valor de la serie

print("\n========== INGRESO DE DATOS ==========\n") # Título del programa

lim = int(input("Ingrese el limite: ")) # Solicita el límite

print(f"La serie fibonacci es: {a}")

while (b <= lim): # Mientras b sea menor o igual al límite
    print(b) # Muestra el valor de b
    c = a + b # Calcula la suma de a y b
    a = b # Actualiza el valor de a
    b = c # Actualiza el valor de b 
    
print("\n========== FIN DEL PROGRAMA ==========\n") # Fin del programa