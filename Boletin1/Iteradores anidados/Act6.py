num = int(input("Dime un numero: "))
cuadrado = ""

for fila in range(num):
    if fila == 0 or fila == num - 1:
        print("*" * num)
    else:
        print("*" + " " * (num - 2) + "*")