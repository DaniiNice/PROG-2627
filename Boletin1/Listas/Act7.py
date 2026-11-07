numeros = []

for i in range(11):
    contador = str(i)
    num = int(input("Dime un numero (" + contador + "/10): "))
    numeros.append(num)

maximo = numeros[0]
minimo = numeros[0]

for i in range(1, len(numeros)):
    if maximo <= numeros[i]:
        maximo = numeros[i]
    elif minimo >= numeros[i]:
        minimo = numeros[i]

print("Max: " + str(maximo))
print("Min: " + str(minimo))