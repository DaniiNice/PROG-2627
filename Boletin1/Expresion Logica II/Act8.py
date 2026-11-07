cuotaPagada = input("Tienes la cuota pagada? (S o N): ")
reservado = input("Tienes una plaza reservada? (S o N): ")

if reservado.upper() != "N" and cuotaPagada.upper() != "N":
    fecha = input("A que hora tienes la reserva? (XX:XX): ")

    hora = int(fecha[:fecha.find(":")])
    min = int(fecha[1 + fecha.find(":"):])

    if hora > 23 or min > 60:
        print("Hora invalida")
    else:
        print("Puedes entrar al gym")

else:
    print("No puedes entrar")