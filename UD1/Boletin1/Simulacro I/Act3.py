meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
dia = int(input("Dime dia:"))
mes = int(input("Dime mes:"))
calculo = 0

for i in range (0, mes-1):
    calculo = calculo + meses [i]
    calculo = calculo + dia
    
print("El día del año es:", dia, "de", mes)
print("Han pasado desde el 1 de enero:", calculo)