arbolesLista = []
arboles = int(input("Numero de arboles: "))

for i in range(1, arboles + 1):
    arbolesLista.append(input(f"Tipo del Arbol {i} (A/B): ").upper())
    arbolesLista.append(int(input(f"Diametro del Arbol {i}: ")))
    arbolesLista.append(int(input(f"Altura del Arbol {i}: ")))

    if arbolesLista[-3] == "B":
        arbolesLista.append(int(input(f"Edad del arbol {i}: ")))
        print(arbolesLista[-4:])
    else:
        print(arbolesLista[-3:])

maximo = arbolesLista[2]
minimo = arbolesLista[2]
pos = arbolesLista[2]
edadMedia = 0
num = 0
m30 = 0

for i in range(len(arbolesLista)):
    if type(arbolesLista[i]) is str:
        if maximo <= arbolesLista[i + 2]:
            maximo = arbolesLista[i + 2]
            pos = i + 2
        elif minimo >= arbolesLista[i + 2]:
            minimo = arbolesLista[i + 2]

        if arbolesLista[i + 2] > 30:
            m30 += 1

    if arbolesLista[i] == "B":
        num += arbolesLista[i + 3]
        edadMedia = num / arboles

print(f"La altura máxima es {maximo}m.")
print(f"La altura mínima es {minimo}m.")
print(f"La media de edad para los de tipo B es {edadMedia} años")
print(f"Existen {m30} árboles en total de más de 30 m.")

if arbolesLista[pos - 2] == "B":
    print(f"Los datos de la altura máxima: {arbolesLista[pos - 2:pos + 2]}")
else:
    print(f"Los datos de la altura máxima: {arbolesLista[pos - 2:pos + 1]}")

print("Resumen de todos los arboles: ")

for i in range(len(arbolesLista)):
    if arbolesLista[i] == "A":
        print(arbolesLista[i:i + 3])
    elif arbolesLista[i] == "B":
        print(arbolesLista[i:i + 4])