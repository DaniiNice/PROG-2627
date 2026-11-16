num = int(input("Dime un numero: "))
cuadrado = ""

for columna in range(num):
    cuadrado += "*"
for fila in range(num):
    print(cuadrado)