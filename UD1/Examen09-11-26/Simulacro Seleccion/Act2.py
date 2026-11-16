import random
bucle = True

print("=====================================")
print("SOMBRERO SELECCIONADOR")
print("=====================================")
print("1. Seleccionar casa para un alumno")
print("2. Mostrar estadísticas")
print("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje inombrable")

opcion = int(input("Opcion elegida: "))

while bucle:
    match opcion:
        case 1:
            print("Ejecutando y seleccionando casa")
            nombre = input("Nombre de alumnado: ")

            casas = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
            casaRandom = random.randint(0, 3)
            casa = casas[casaRandom]
            
            print(f"El Sombrero dice que {nombre} pertenece a {casa}")
            bucle = False

        case 2:
            print("Ejecutando y mostrar estadísticas")
            bucle = False

        case _:
            opcion = int(input("Debe elegir una opción correcta: "))