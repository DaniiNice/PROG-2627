import random

numeros_aleatorios = []

for i in range(5):
    numero = random.randint(0, 8)
    numeros_aleatorios.append(numero)

print(numeros_aleatorios)