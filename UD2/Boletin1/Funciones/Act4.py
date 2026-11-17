def calculaTemperaturaMedia(maximaE, minimaE):
    media = (minimaE + maximaE) / 2
    return media

veces = int(input("Cuantos dias quieres calcular la temperatura: "))

for i in range(1, veces + 1):
    maxima = int(input(f"Dime la temperatura maxima del dia {i}: "))
    minima = int(input(f"Dime la temperatura minima del dia {i}: "))
    resultado = calculaTemperaturaMedia(maxima, minima)
    print(f"La media de la temperatura del dia {i} es {resultado}")