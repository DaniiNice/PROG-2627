numeros = []

for i in range(10):
    num = int(input("Dime un numero (" + str(i) + "/10): "))
    numeros.append(num)

print("Lista ordenada: " + str(numeros))
print("Lista inversa: " + str(numeros[::-1]))