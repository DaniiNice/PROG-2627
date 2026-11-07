import random

num1 = random.randint(0 , 4)
num2 = random.randint(0 , 4)
respuesta = num1 + num2
intento = int(input(f"Calcula {num1} + {num2}: "))

while respuesta != intento:
    intento = int(input("Intentalo de nuevo: "))
    
print("Correcto")