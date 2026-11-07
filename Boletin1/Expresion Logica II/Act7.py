pagoRealizado = float(input("Cuanto dinero vas a enviar?: "))
pagosTotal = float(input("Cuanto dinero en total enviaste hoy? (Sin contar el de ahora): "))

if pagoRealizado >= 0.50 and pagoRealizado <= 1000 and pagoRealizado + pagosTotal <= 2000:
    print("Enviado con exito")
else:
    print("No cumples los requisitos para enviar")