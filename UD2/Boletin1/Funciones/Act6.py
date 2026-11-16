def calcularMax (numeros):
    maximo = numeros[0]

    for i in range(1, len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros[i]

    return maximo

def calcularLista ():
    numerosN = []

    for i in range(1, 11):
        numerosN.append(int(input(f"Dime el numero {i}: ")))

    return numerosN

listaN = calcularLista()
print(calcularMax(listaN))