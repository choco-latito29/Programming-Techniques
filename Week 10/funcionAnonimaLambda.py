# NORMAL
def suma(a, b):
    return a + b

# ANONIMA
suma = lambda a, b: a + b

# EJEMPLO DE USO
suma = lambda x, y: x + y

resultado = suma(3, 5)
print(resultado)

# FUNCION LAMBDA ENTRADA DE FUNCION NORMAL
def suma(funcionLambda):
    return funcionLambda(2, 4)

suma(lambda a, b: a + b)

# FUNCION NORMAL DE ENTRADA LAMBDA
def suma(a, b):
    return a + b

(lambda a, b: suma(a, b))(2, 4)