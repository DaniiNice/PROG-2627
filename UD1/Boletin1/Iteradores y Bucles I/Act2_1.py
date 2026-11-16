error = True

while error:
    num = int(input("Dime un numero (negativo para terminar): "))
    if num >= 0:
        elevado = num ** 2
        print(f"{num} elevado a 2 es: {elevado}")
    else:
        error = False