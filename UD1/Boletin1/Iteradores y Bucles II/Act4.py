num = int(input("Dime un numero (0 para terminar): "))
numProgreso = ""

while num != 0:
    numProgreso += f"{num} "
    num = int(input("Dime un numero (0 para terminar): "))
print(f"Numeros mencionados: {numProgreso}")