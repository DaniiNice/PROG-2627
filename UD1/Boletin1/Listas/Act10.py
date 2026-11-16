lista = []

for i in range(1, 16):
    num = int(input(f"Dime un numero {i}/15: "))
    lista.append(num)

ultimo = lista[len(lista) - 1]
#lista.pop(ultimo - 1)
#lista.insert(0, ultimo)
lista.insert(0, ultimo)
lista_sin_ultimo = lista[0:len(lista) - 1]
print(lista_sin_ultimo)