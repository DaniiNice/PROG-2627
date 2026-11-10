nombres = []
tipos = []
vidas = []
danios = []
brawlers = int(input("Cuantos brawlers vas a registrar: "))
indice = 1

for i in range(brawlers):
    tipoBrawler = ""
    bucle = True
    nombres.append(input("Nombre del brawler: "))

    while bucle:
        if tipoBrawler == "T" or tipoBrawler == "N":
            if tipoBrawler == "T":
                tipos.append("Tanque")
            else:
                tipos.append("Normal")
            bucle = False
        else:
            tipoBrawler = input("Tipo del brawler - T o N (tanque o normal): ").upper()

    vidas.append(int(input("Cuanta vida tiene: ")))
    danios.append(int(input("Cuanto daño tiene: ")))

    print(f"Brawler {indice}: {nombres[i]} ({tipos[i]}) - Vida: {vidas[i]} - Daño: {danios[i]}")
    indice += 1
