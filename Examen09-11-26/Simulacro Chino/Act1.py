import random
apuestas = ["P", "I"]
numHumano = int(input("Cuantas piedras quieres mostrar (0 al 5): "))
numMaquina = random.randint(0, 5)
RandomMaquina = random.randint(0, 1)
apuestaMaquina = apuestas[RandomMaquina]
parMaquinaparHumano = False
parMaquina = False

if numHumano >= 0 and numHumano <= 5:
    if numHumano % 2 == 0:
        parHumano = True

    if numMaquina % 2 == 0:
        parMaquina = True

    apuestaHumano = input("El contrincante tiene P o I? (par o impar): ").upper()

    if apuestaHumano == "P" and parMaquina:
        print("Felicidades, acertaste!")
    else:
        print("Fallaste")

    if apuestaMaquina == "P" and parHumano:
        print(f"El contrincante ha intentado {apuestaMaquina} y acertado!")
    else:
        print(f"El contrincante ha intentado {apuestaMaquina} y fallado")