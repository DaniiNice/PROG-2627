lista = []
error = True
n = 20

for i in range(1, 16):
    num = int(input(f"Dime un numero {i}/15: "))
    lista.append(num)

while error:
    if n > len(lista):
        n = int(input("Cuantas veces va a rotar (menor que 15): "))
    else:
        error = False

# lista[-n:] toma los últimos 'n' elementos
# lista[:-n] toma el resto de la lista
lista_rotada = lista[-n:] + lista[:-n]

print("Lista rotada n veces:", lista_rotada)