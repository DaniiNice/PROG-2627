numReal = int(input("Dime un numero positivo: "))
numTotal = 1
numProgreso = "1"
numOrden = 2

for i in range(1, numReal + 1):
    numTotal = numTotal * i
    numProgreso += f"*{numOrden}"
    numOrden += 1


print(f"{numReal}! = {numProgreso} = {numTotal}")