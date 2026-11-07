lista = []

for i in range(1, 4):
        num = int(input(f"Dime un numero para el grupo {i}: "))
        lista.append(num)

for i in range(len(lista)):
        print(lista[i])