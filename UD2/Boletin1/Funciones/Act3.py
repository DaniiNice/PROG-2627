def calculaTemperaturaMedia (maxima, minima):
    media = (minima + maxima) / 2
    return media

maxima = int(input("Dime la temperatura maxima: "))
minima = int(input("Dime la temperatura minima: "))
resultado = calculaTemperaturaMedia(maxima, minima)

print(resultado)