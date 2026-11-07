gananciasCartas = float(input("Cuanto has ganado con las cartas?: "))
mantenimientoGastos = float(input("Cuanto tienes que pagar por mantenimiento?: "))
gananciaFinal = gananciasCartas - mantenimientoGastos

if gananciaFinal >= 1200:
    print("Tienes una buena ganancia")
elif gananciaFinal >= 1000:
    print("Tienes una ganancia decente")
else:
    print("Tienes una mala ganancia")