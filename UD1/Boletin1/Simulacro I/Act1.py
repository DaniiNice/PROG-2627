bucle = True

while bucle:
    grupo = []

    for i in range(1, 4):
        num = int(input(f"Dime el grupo {i}: "))
        grupo.append(num)

    if grupo[0] < grupo[1] and grupo[1] < grupo[2]:
        print("creciente")
    elif grupo[0] > grupo[1] and grupo[1] > grupo[2]:
        print("decreciente")
    else:
        print("desordenados")

    if grupo[0] == 0 and grupo[1] == 0 and grupo[2] == 0:
        print("FIN")
        bucle = False