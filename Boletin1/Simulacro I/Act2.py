lista = []
bucle = True
creciente = False
decreciente = False

while bucle:
    num = int(input(f"Dime un numero (0 para parar): "))

    if num == 0:
        print("FIN")
        bucle = False
    else:
        lista.append(num)

    if len(lista) > 1:
        for i in range(len(lista)):
            if lista[i] < lista[i + 1]:
                creciente = True
            elif lista[i] > lista[i + 1]:
                decreciente = True

if creciente:
    print("Creciente")
elif decreciente:
    print("Decreciente")
else:
    print("Desordenado")