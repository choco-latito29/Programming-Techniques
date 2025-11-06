import Bookshops.operacionesAritmeticas as calculadora
from Bookshops.operacionesAritmeticas import restar

num1 = 5
num2 = 3

s = calculadora.sumar(num1, num2)
r = restar(num1, num2)

print(f"La suma es: {s}")
print(f"La resta es: {r}")