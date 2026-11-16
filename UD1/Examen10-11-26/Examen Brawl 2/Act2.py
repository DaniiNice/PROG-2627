nombres = []
rarezas = []
trofeos = []
numPartidas = []
bucle = True
pos = 0

while bucle:
    print("""======= BRAWL STARTS REGISTRO =======
    1. Guardar datos del brawler
    2. Registrar partida
    3. Mostrar resumen
    4. Terminar programa
    Selecciona una opción""")

    opcion = int(input("Opcion: "))

    match opcion:
        case 1:
            print("Guardando los datos de un brawler")
            nombres.append(input("Nombre del brawler: "))
            bucle2 = True

            while bucle2:
                rareza = input("Rareza del brawler - C, R, E o L (Comun, Rara, Epico o Legendario): ").upper()

                if rareza in ["C", "R", "E", "L"]:
                    rarezas.append(rareza)
                    bucle2 = False

            trofeos.append(int(input("Trofeos iniciales del brawler: ")))
            numPartidas.append(0)

            print(f"Registrados los datos del brawler {nombres[pos]}")
            pos += 1

        case 2:
            print("Registrando")

        case 3:
            print("Resumiendo")

        case 4:
            print("fin")
            bucle = False

        case _:
            print("Opcion no valida. Intentelo de nuevo")