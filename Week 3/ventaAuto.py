from datetime import datetime # Importando la librería datetime para manejar fechas

############# INICIO DE ENTRADA DE DATOS #############
print("\n========== INGRESO DE DATOS ==========\n") # Título del programa

print("********* CLIENTE *********") # Datos del cliente
dni = int(input("Ingrese su DNI: ")) # DNI del cliente
apellido = input("Ingrese su apellido: ") # Apellido del cliente
nombre = input("Ingrese su nombre: ") # Nombre del cliente
datosCliente = nombre + " " + apellido # Concatenando nombre y apellido

print("\n********* VEHÍCULO *********") # Datos del vehículo
marca = input("Ingrese la marca del vehículo: ") # Marca del vehículo
modelo = input("Ingrese el modelo del vehículo: ") # Modelo del vehículo
año = int(input("Ingrese el año del vehículo: ")) # Año del vehículo
precioDolares = float(input("Ingrese el precio del vehículo en dólares: ")) # Precio del vehículo en dólares

print("********* TIPO DE CAMBIO *********") # Tipo de cambio
tipoCambio = float(input("Ingrese el tipo de cambio a soles: ")) # Tipo de cambio a soles
############# FIN DE ENTRADA DE DATOS #############

############# INICIO DE PROCESOS #############
#Calculando
montoImpuestoDolar = precioDolares * 0.19 # Impuesto del 19% en dólares
montopagoDolares = precioDolares + montoImpuestoDolar # Monto total a pagar en dólares
montoImpuestoSoles = montopagoDolares * tipoCambio # Impuesto del 19% en soles
montopagoSoles = montopagoDolares * tipoCambio # Monto total a pagar en soles

# Generando el comprobante de pago
numeroComprobante = input("Ingrese el número de comprobante: ") # Número de comprobante
fechaAhora = datetime.now() # Fecha actual
año = fechaAhora.year # Año actual
mes = fechaAhora.month # Mes actual
dia = fechaAhora.day # Día actual
############## FIN DE PROCESOS #############

############# SALIDA DE DATOS #############
print("\n========== REPORTE DE DATOS ==========\n") # Título del reporte
print("********* COMPROBANTE DE PAGO *********") # Título del comprobante
print(f"Número de comprobante: {numeroComprobante}") # Muestra el número de comprobante
print(f"DNI del Cliente: {dni}") # Muestra el DNI del cliente
print(f"Cliente: {datosCliente}") # Muestra el nombre completo del cliente
print(f"Fecha de emisión: {dia}/{mes}/{año}") # Muestra la fecha de emisión
print(f"Monto a pagar en dólares: $ {montopagoDolares:.2f}") # Muestra el monto a pagar en dólares
print(f"Impuesto en dólares (19%): $ {montoImpuestoDolar:.2f}") # Muestra el impuesto en dólares
print(f"Monto a pagar en soles: S/. {montopagoSoles:.2f}") # Muestra el monto a pagar en soles
print(f"Impuesto en soles (19%): S/. {montoImpuestoSoles:.2f}") # Muestra el impuesto en soles
print("\n¡Felicitaciones por su compra...!") # Mensaje de felicitación

print("\n========== FIN DEL PROGRAMA ==========\n") # Fin del programa