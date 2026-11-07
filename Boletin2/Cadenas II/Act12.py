num = input("Dime un numero: ")
posicion = 0
numPuntos = ""

for i in range(len(num)):
    numPuntos += num[i]
    posicion += 1

    if posicion >= 3 and i != len(num) - 1:
        numPuntos += "."
        posicion = 0

print(numPuntos)