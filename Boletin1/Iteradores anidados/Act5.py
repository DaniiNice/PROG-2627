num = int(input("Dime un numero: "))
cuadrado = ""

for fila in range(num):
    # Si es la primera fila o la última fila, se pinta completa
    if fila == 0 or fila == num - 1:
        print("*" * num)
    # Si es una fila intermedia, se pinta solo el borde
    else:
        # Un asterisco al principio, espacios en medio, y un asterisco al final
        # Usamos num - 2 porque el primero y el último ya ocupan espacio
        print("*" + " " * (num - 2) + "*")