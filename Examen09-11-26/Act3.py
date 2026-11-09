import random
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

                casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
                casaRandom = random.randint(0, 3)
                casa = casas[casaRandom]

                if nombre != "voldemort":
                    print(f"El Sombrero dice que {nombre} pertenece a {casa}")
                else:
                    bucle = False

            case 2:
                print("Ejecutando y mostrar estadísticas")

if opcion == 1 and nombre == "voldemort":
    print("Apparition, transpórtame a otro sitio")