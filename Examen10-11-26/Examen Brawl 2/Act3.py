bucle = True

while bucle:
    print("""======= BRAWL STARTS REGISTRO =======
    1. Guardar datos del brawler
    2. Registrar partida
    3. Mostrar resumen
    4. Terminar programa
    Selecciona una opción""")

    bucle2 = True
    opcion = int(input("Opcion: "))

    match opcion:
        case 1:
            print("Guardando los datos de un brawler")
            nombreBrawler = input("Nombre del brawler: ")

            while bucle2:
                rarezaBrawler = input("Rareza del brawler - C, R, E o L (Comun, Rara, Epico o Legendario): ").upper()

                if rarezaBrawler in ["C", "R", "E", "L"]:
                    bucle2 = False

            trofeosBrawler = (int(input("Trofeos iniciales del brawler: ")))
            numPartidas = 0

            print(f"Registrados los datos del brawler {nombreBrawler}")

        case 2:
            print("Registrando")
            trofeosPartida = 0
            
            while bucle2:
                modoJuego = input("Modo de juego - G, B, N o S (Atrapagemas, Balon Brawl, Noqueo o Supervivencia): ").upper()

                if modoJuego in ["G", "B", "N", "S"]:
                    bucle2 = False

            if modoJuego in ["G", "B", "N"]:
                resultado = input("Resultado de la partida - V, D o E (Victoria, Derrota o Empate): ").upper()

                if resultado == "V":
                    trofeosBrawler += 10
                    trofeosPartida += 10
                elif resultado == "D":
                    trofeosBrawler -= 5
                    trofeosPartida -= 5

            elif modoJuego == "S":
                posicion = int(input("Posicion de la partida: "))
                trofeosBrawler += 12 - 2 * posicion
                trofeosPartida += 12 - 2 * posicion

            print(f"El brawler {nombreBrawler} ha conseguido: {trofeosPartida} en esta partida, quedando su total de trofeos a {trofeosBrawler}")
            numPartidas += 1

        case 3:
            print("Resumiendo")

        case 4:
            print("fin")
            bucle = False

        case _:
            print("Opcion no valida. Intentelo de nuevo")