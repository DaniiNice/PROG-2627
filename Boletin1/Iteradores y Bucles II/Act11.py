import random

numRandom = random.randint(0, 10)
numRandom2 = random.randint(0, 10)
solucion = numRandom + numRandom2
numPersona = int(input(f"{numRandom} + {numRandom2} = "))

while numPersona != solucion:
    numPersona = int(input(f"Incorrecto, intenta de nuevo {numRandom} + {numRandom2} = "))
print("Bien hecho!")