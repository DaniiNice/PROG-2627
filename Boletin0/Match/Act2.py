dia = input("Dime el dia actual de la semana: ")

match dia:
    case "LUNES" | "Lunes" | "lunes": 
        print("\n-------------------")
        print("       LUNES      ")
        print("-------------------")
        print("8-9 FOL")
        print("9-10 EDE")
        print("10-11 PROG")
        print("11-11:30 Recreo")
        print("11:30-12 Progr")
        print("12-14 BBDD")
        print("-------------------")
    case "Sábado" | "domingo": 
        print("Día de estudio y reflexión")
    case _:
        print("El valor es incorrecto")