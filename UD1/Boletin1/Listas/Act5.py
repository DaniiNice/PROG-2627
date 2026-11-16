import random

numeros = []
cuadrados_numeros = []
cubos_numeros = []

for i in range(20):
    num_aleatorio = random.randint(0, 100)
    numeros.append(num_aleatorio)

for i in range(len(numeros)):
    cuadrados_numeros.append(i ** 2)

for i in range(len(numeros)):
    cubos_numeros.append(i ** 3)

print("Numero | Cuadrado | Cubo")
print("-" * 30)

for i in range(20):
    print(f"{numeros[i]}     |     {cuadrados_numeros[i]}     |     {cubos_numeros[i]}")