numer = []

def calcularMax (numeros):
    maximo = 0

    for i in range(len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros[i]

    return maximo

for i in range(1, 11):
    numer.append(int(input(f"Dime el numero {i}: ")))

print(calcularMax(numer))