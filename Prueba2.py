listaNumeros = []
creciente = True
decreciente = True
bucle = True
posicion = 0

while bucle:
    num = int(input("Dime un numero (0 para terminar): "))
    #Es necesario poner -1 porque comparamos cada número con el siguiente.
    #El último número no tiene otro detrás, asi evitamos salirnos de la lista.
    if num == 0:
        print("FIN")
        bucle = False
    else:
        listaNumeros.append(num)

    if listaNumeros[posicion] >= listaNumeros[posicion + 1]:
        creciente = False

    if listaNumeros[posicion] <= listaNumeros[posicion + 1]:
        decreciente = False

    posicion = posicion + 1

if creciente:
    print("Creciente")
elif decreciente:
    print("Decreciente")
else:
    print("Desordenados")