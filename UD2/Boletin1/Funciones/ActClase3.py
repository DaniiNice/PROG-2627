def calculaHoras(segundosIni):
    return segundosIni // 3600

def calculaMinutos(segundosIni, horas):
    segundosRestantes = segundosIni - 3600 * horas
    return segundosRestantes // 60

def calculaSegundos(segundosIni, horas, minutos):
    return segundosIni - 3600 * horas - 60 * minutos

def calculaTiempoDeSegundos(segundosIni):
    horas = calculaHoras(segundosIni)
    minutos = calculaMinutos(segundosIni, horas)
    segundosFinales = calculaSegundos(segundosIni, horas, minutos)
    return [horas, minutos, segundosFinales]

segundosIniciales = int(input("Dime cuantos segundos totales quieres convertir: "))
resultado = calculaTiempoDeSegundos(segundosIniciales)

print(f"Horas: {resultado[0]}, Minutos: {resultado[1]}, Segundos: {resultado[2]}")