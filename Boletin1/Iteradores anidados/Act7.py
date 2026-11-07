num = int(input("Dime un numero: "))
cuadrado = ""

for fila in range(num):
    if num < 2:
        print("*")
    elif fila == 0 or fila == num - 1:
        print("*" + "#" * (num - 2) + "*")
    else:
        print("*" * num)