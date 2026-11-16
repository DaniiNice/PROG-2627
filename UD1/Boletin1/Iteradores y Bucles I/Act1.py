maxNum = int(input("Dime un numero: "))

while True:
    if maxNum >= 1:
        realMaxNum = maxNum + 1
        for i in range(1, realMaxNum, 1):
            print(i)
        break
    else:
        maxNum = int(input("El numero no puede ser menor que 1: "))