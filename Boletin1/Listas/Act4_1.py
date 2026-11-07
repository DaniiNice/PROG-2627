alumnos=["alumno 1", "alumno 2", "alumno 3", "alumno 4"]
edades=[15,18,19,25]
altura=[1.80,1.60,1.55,1.64]

for i in range(len(edades)):
    if edades[i]>=18:
        print(alumnos[i],altura[i])

sumaAlturas = 0

for i in range (len(altura)):
    sumaAlturas = sumaAlturas + altura[i]

media = sumaAlturas/len(altura)

for i in range(len(altura)):
    if altura[i] > media:
        print(alumnos[i], altura[i])