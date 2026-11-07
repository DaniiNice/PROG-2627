valorfin = int(input("A"))
num = 0

if valorfin >= 0:
    for i in range(1, valorfin, 1):
        num = num + i
    print(num)
else:
    print("Numero Incorrecto")