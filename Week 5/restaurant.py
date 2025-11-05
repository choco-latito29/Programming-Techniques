print("\n========== CÁLCULO DE CUENTA DE RESTAURANTE ==========\n")

consumo = float(input("Ingrese el monto del consumo (S/.): "))

if (consumo > 0):
    
    if consumo <= 30:
        dcto = 0.10
    else:
        dcto = 0.20

    montoDcto = consumo * dcto
    subtotal = consumo - montoDcto
    impuesto = subtotal * 0.18
    totalPagar = subtotal + impuesto

    print("\n========== RECIBO DETALLADO ==========\n")
    print(f"Consumo:          S/. {consumo:.2f}")
    print(f"Descuento:        S/. {montoDcto:.2f}")
    print(f"Subtotal:         S/. {subtotal:.2f}")
    print(f"Impuesto (18%):   S/. {impuesto:.2f}")
    print("---------------------------------------")
    print(f"IMPORTE A PAGAR:  S/. {totalPagar:10.2f}")

else:
    print("[ERROR] El monto del consumo debe ser mayor a cero.")