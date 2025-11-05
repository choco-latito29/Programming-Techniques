a = 0
b = 1

print("\n========== INGRESO DE DATOS ==========\n")

lim = int(input("Ingrese el limite: "))

print(f"La serie fibonaci es: {a}")

while (b <= lim):
    print(b)
    c = a + b
    a = b
    b = c