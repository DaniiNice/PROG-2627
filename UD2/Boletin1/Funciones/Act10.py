def convertirMinutos(segundosE):
    minutos = segundosE // 60
    return minutos

def convertirHoras(minutosE):
    horas = minutosE // 3600
    return horas

segundos = int(input("Dime una cantidad de segundos: "))
print(f"{convertirHoras(segundos)}h {convertirMinutos(segundos)}m {segundos}s")