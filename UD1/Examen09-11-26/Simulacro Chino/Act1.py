import random
apuestas = ["P", "I"]
bucle = True

while bucle:
    numHumano = int(input("Cuantas piedras quieres mostrar (0 al 5): "))
    numMaquina = random.randint(0, 5)
    RandomMaquina = random.randint(0, 1)
    apuestaMaquina = apuestas[RandomMaquina]
    parMaquina = False
    parHumano = False

    if numHumano >= 0 and numHumano <= 5:
        if numHumano % 2 == 0:
            parHumano = True

        if numMaquina % 2 == 0:
            parMaquina = True

        apuestaHumano = input("El contrincante tiene P o I? (par o impar): ").upper()

        if (apuestaHumano == "P" and parMaquina) or (apuestaHumano == "I" and not parMaquina):
            print("Felicidades, acertaste!")
        else:
            print("Fallaste")

        if (apuestaMaquina == "P" and parHumano) or (apuestaMaquina == "I" and not parHumano):
            print(f"El contrincante ha intentado {apuestaMaquina} y acertado!")
        else:
            print(f"El contrincante ha intentado {apuestaMaquina} y fallado")

        if numHumano == numMaquina:
                bucle = False
    else:
        print("Número fuera de rango. Debe ser entre 0 y 5")
print("fin")