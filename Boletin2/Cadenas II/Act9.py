num = input("Dime un numero: ")
posicion = 0
numPuntos = ""

for i in range(len(num) - 1, -1, -1):
    numPuntos = num[i] + numPuntos
    posicion += 1

    if posicion == 3 and i != 0:
        numPuntos = "." + numPuntos
        posicion = 0

print(numPuntos)