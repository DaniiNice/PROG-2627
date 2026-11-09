import random
casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
numAlumCasa = [0, 0, 0, 0]
alumnos = []
nombre = ""
opcion = 0
bucle = True

while bucle:
    if opcion == 1 and nombre == "voldemort":
        bucle = False

    print("=====================================")
    print("SOMBRERO SELECCIONADOR")
    print("=====================================")
    print("1. Seleccionar casa para un alumno")
    print("2. Mostrar estadísticas")
    print("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje inombrable")

    if opcion != 1 or opcion != 2:
        opcion = int(input("Opcion elegida: "))

        match opcion:
            case 1:
                print("Ejecutando y seleccionando casa")

                nombre = input("Nombre de alumnado: ").lower()
                alumnos.append(nombre)
                casaRandom = random.randint(0, 3)
                casa = casas[casaRandom]
                numAlumCasa[casaRandom] += 1

                if nombre != "voldemort":
                    print(f"El Sombrero dice que {nombre} pertenece a {casa}")
                else:
                    bucle = False

            case 2:
                print("Ejecutando y mostrar estadísticas")
                print(f"Total de alumnos: {len(alumnos)}")
                print(f"Gryffindor: {numAlumCasa[0]}")
                print(f"Slytherin: {numAlumCasa[1]}")
                print(f"Hufflepuff: {numAlumCasa[2]}")
                print(f"Ravenclaw: {numAlumCasa[3]}")

if opcion == 1 and nombre == "voldemort":
    print("Apparition, transpórtame a otro sitio")