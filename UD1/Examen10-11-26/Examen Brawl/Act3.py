nombres = []
tipos = []
vidas = []
danios = []
indice = 1

for i in range(2):
    print("Registrando")
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

print("Batalla")
danioBrawler1 = danios[0]
danioBrawler2 = danios[1]
vidaBrawler1 = vidas[0]
vidaBrawler2 = vidas[1]
favorito = nombres[0]
ataquesBrawler1 = 0
ataquesBrawler2 = 0
rondaGanada1 = 1
rondaGanada2 = 1
ronda = 1
batallaTerminada = False
vivoBrawler1 = True
vivoBrawler2 = True
    
while not batallaTerminada:
    if tipos[0] == "Tanque":
        danioBrawler2 = danios[1] * 80 // 100
    else:
        danioBrawler2 = danios[1]

    if tipos[1] == "Tanque":
        danioBrawler1 = danios[0] * 80 // 100
    else:
        danioBrawler1 = danios[0]
    
    if ronda % 3 == 0:
        danioBrawler1 *= 2
        danioBrawler2 *= 2

    if vidaBrawler2 >= danioBrawler1:
        vidaBrawler2 -= danioBrawler1
        ataquesBrawler1 += 1
    elif vivoBrawler2:
        ataquesBrawler1 += 1
        vivoBrawler2 = False
        rondaGanada1 = ronda
    
    if vidaBrawler1 >= danioBrawler2:
        vidaBrawler1 -= danioBrawler2
        ataquesBrawler2 += 1
    elif vivoBrawler1:
        ataquesBrawler2 += 1
        vivoBrawler1 = False
        rondaGanada2 = ronda

    print(f"Ronda {ronda} -- {nombres[0]}: {vidaBrawler1} | {nombres[1]}: {vidaBrawler2}")
    ronda += 1

    if not vivoBrawler1 and not vivoBrawler2:
        batallaTerminada = True

if ataquesBrawler1 > ataquesBrawler2:
    favorito = nombres[1]
elif ataquesBrawler2 > ataquesBrawler1:
    favorito = nombres[0]
else:
    favorito = "Empate"

if favorito == nombres[0]:
    print(f"Vida restante de {nombres[0]}: {vidaBrawler1 * 100 // vidas[0]}%")
    print(f"Gana {nombres[0]} en la ronda {rondaGanada1}")
elif favorito == nombres[1]:
    print(f"Vida restante de {nombres[1]}: {vidaBrawler2 * 100 // vidas[1]}%")
    print(f"Gana {nombres[1]} en la ronda {rondaGanada2}")

print(f"{nombres[0]} necesita {ataquesBrawler1} ataques para derrotar a {nombres[1]}")
print(f"{nombres[1]} necesita {ataquesBrawler2} ataques para derrotar a {nombres[0]}")
print(f"Favorito: {favorito}")