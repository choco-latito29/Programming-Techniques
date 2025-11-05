producto = 1

print("="*50)

n = int(input("Ingrese el número para factorial: "))

for i in range (n):
    i = i + 1
    producto = producto * i

print("\n========== REPORTE ==========\n")
print(f"El factorial de {n} es {producto}")