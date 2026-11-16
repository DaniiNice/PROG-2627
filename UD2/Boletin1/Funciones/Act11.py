bucle = True

def menu ():
    print("""======== Convertidor ========
    1. Convertir a Segundos
    2. Convertir a Minutos
    3. Convertir a Horas
    (-1) Salir del programa
===============================""")

def convertirMinutos (segundosE):
    minutos = segundosE // 60
    return minutos

def convertirHoras (minutosE):
    horas = minutosE // 3600
    return horas

while bucle:
    segundos = int(input("Dime una cantidad de segundos: "))
    menu()
    opcion = int(input("Opcion: "))

    match opcion:
        case 1:
            print(f"{segundos}s")
            
        case 2:
            print(f"{convertirMinutos(segundos)}m")

        case 3:
            print(f"{convertirHoras(segundos)}h")

        case -1:
            print("FIN")
            bucle = False

        case _:
            print("Intentalo de nuevo")