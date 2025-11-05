palabra = input("Ingrese una palabra (o cualquier texto): ")

conteo = 0

for i in palabra:
    conteo = conteo + 1

print(f"El número de letras es: {conteo}")



### Otra forma de hacerlo ###

palabra = input("Ingrese una palabra (o cualquier texto): ")

print(f"El número de letras es: {len(palabra)}")

### Otra forma de hacerlo ###

frase = "Hola Mundo"

conteo = 1

for i in frase:
    if i == " ":
        conteo += 1

print(f"El número de palabras es: {conteo}")

