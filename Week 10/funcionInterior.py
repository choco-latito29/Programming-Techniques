print("=" * 50)

def funcionExterna():
    def funcionInterna():
        return "Ejemplo de funcion Interior"
    
    return funcionInterna()

print(funcionExterna())