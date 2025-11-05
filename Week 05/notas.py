"""
iNGRESAMOS 4 NOTAS TIPO ENTERO
INGRESAR NOTA EXTRA
REEMPLAZAR LA NOTA EXTRA A LA NOTA MAS BAJA
MOSTRAR LA NOTA MAS BAJA 
MOSTRAR PROMEDIO ANTERIOR
MOSTRAR NUEVO PROMEDIO
"""

print("\n========== CÁLCULO DE PROMEDIO DEL ALUMNO ==========\n")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

promedio_inicial = (nota1 + nota2 + nota3 + nota4) / 4
print(f"El promedio inicial es: {promedio_inicial:.2f}")

nota_baja = min(nota1, nota2, nota3, nota4)
print(f"La nota mas baja es: {nota_baja}")

opcion = input("¿Desea ingresar una nota de tarea adicional para reemplazar la nota más baja? (SI/NO): ").upper()

if opcion == "SI" or opcion == "SÍ":
    
    nota_extra = float(input("Ingrese la nota de la tarea adicional: "))
    
    if nota1 == nota_baja:
        nota1 = nota_extra
    elif nota2 == nota_baja:
        nota2 = nota_extra
    elif nota3 == nota_baja:
        nota3 = nota_extra
    elif nota4 == nota_baja:
        nota4 = nota_extra
        
    nuevo_promedio = (nota1 + nota2 + nota3 + nota4) / 4
    
    print(f"\nSe reemplazó la nota {nota_baja} por {nota_extra}.")
    print(f"Las nuevas notas son: {nota1}, {nota2}, {nota3}, {nota4}")
    print(f"El nuevo promedio es: {nuevo_promedio:.2f}")

else:
    print("\nNo se realizó ninguna modificación en las notas.")

print("\n--- Fin del Programa ---")