nombres = []
puntuaciones = []
generos = []
bucle = True

while bucle:
    print("""Selecciona una de las siguientes opciones (R, E, S)
    R. Registrar juegos
    E. Mostrar estadísticas
    P. Mejor Puntuación
    S. Salir del programa""")

    opcion = input("Opcion: ").upper()

    match opcion:
        case "R":
            print("Registrando")
            juegos = int(input("Cuantos juegos quieres registrar: "))

            for i in range(1, juegos + 1):
                nombres.append(input(f"Nombre del juego ({i}/{juegos}): "))
                puntuaciones.append(float(input(f"Puntuacion del juego ({i}/{juegos}): ")))
                generos.append(input(f"Genero del juego ({i}/{juegos}): "))

        case "E":
            print("Estadísticas")
            print("Tu colección de juegos PSP:")

            for i in range(len(nombres)):
                print(f"{nombres[i]} | Puntuacion: {puntuaciones[i]} | Genero: {generos[i]}")

        case "P":
            print("Mayor puntuacion")
            mayor_puntuacion = puntuaciones[0]
            indice_mayor = 0

            for i in range(len(nombres)):
                if puntuaciones[i] > mayor_puntuacion:
                    mayor_puntuacion = puntuaciones[i]
                    indice_mayor = i

            print(f"{nombres[indice_mayor]} | Puntuacion: {puntuaciones[indice_mayor]} | Genero: {generos[indice_mayor]}")

        case "S":
            print("fin")
            bucle = False

        case _:
            print("Opcion no valida. Intentelo de nuevo")