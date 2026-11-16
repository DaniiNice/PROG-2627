puntosConseguidos = int(input("Cuantos puntos tienes?: "))
vidasRestantes = int(input("Cuantas vidas te quedan?: "))

if puntosConseguidos >= 1000 and vidasRestantes >= 1:
    print("Pasas de nivel")
else:
    print("No pasas de nivel")