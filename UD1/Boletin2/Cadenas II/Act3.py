opcion = int(input("Elige: \n 1. Frase por trozos \n Otro. Cantidad caracteres \n - "))

match opcion:
    case 1:
        frase2 = input("Dime una frase: ")
        
        for i in range(len(frase2)):
            print(frase2[i])
            
    case _:
        frase = input("Dime una frase: ").lower()
        letraBuscada = input("Dime una letra a buscar: ").lower()
        encontrada = 0
        porcentaje = 0

        for i in frase:
            if letraBuscada == i:
                encontrada += 1

        if len(frase) > 0:
            porcentaje = (encontrada / len(frase)) * 100
            print(f"La letra '{letraBuscada}' aparece {encontrada} veces, lo que representa un {porcentaje}% de la frase")
        else:
            print("No se introdujo ninguna frase")