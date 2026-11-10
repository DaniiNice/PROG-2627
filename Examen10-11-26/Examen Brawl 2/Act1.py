bucle = True

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

        case 2:
            print("Registrando")

        case 3:
            print("Resumiendo")

        case 4:
            print("fin")
            bucle = False

        case _:
            print("Opcion no valida. Intentelo de nuevo")