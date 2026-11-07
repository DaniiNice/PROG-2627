opcion = int(input("Elige: \n 1. Frase por trozos \n Otro. Cantidad caracteres \n - "))

match opcion:
    case 1:
        for i in range(len(opcion)):
            print(opcion[i])
    case _:
        frase = input("Dime una frase: ").lower()
        letraBuscada = input("Dime una letra a buscar: ").lower()
        encontrada = 0

        for i in frase:
            if letraBuscada == i:
                encontrada += 1

        print(f"Se ha encontrado \"{letraBuscada}\" {encontrada} veces")