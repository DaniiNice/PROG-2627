numMes = int(input("Dime el numero del mes: "))
dia = int(input("Dime el dia numerico: "))
estacion = ""

match numMes:
    case 1 | 2 | 3: 
        if dia <= 20:
            estacion = "Invierno"
        elif dia >= 20:
            estacion = "Primavera"
    case 4 | 5 | 6:
        if dia <= 20:
           estacion = "Primavera"
        elif dia >= 20:
            estacion = "Verano"
    case 7 | 8 | 9:
        if dia <= 20:
            estacion = "Verano"
        elif dia >= 20:
            estacion = "Otoño"
    case 10 | 11 | 12:
        if dia <= 20:
            estacion = "Otoño"
        elif dia >= 20:
            estacion = "Invierno"
    case _:
        print("Valor Incorrecto")
print(estacion)