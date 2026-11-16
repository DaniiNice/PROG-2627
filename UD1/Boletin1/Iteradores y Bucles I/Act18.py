numReal = int(input("Dime un numero positivo: "))
numTotal = 1

for i in range(1, numReal + 1):
    # Factorial es todos los numeros anteriores del numero indicado hasta 1
    numTotal = numTotal * i  # Multiplicamos el acumulado por el número actual i
print(f"El factorial de {numReal} es: {numTotal}")
