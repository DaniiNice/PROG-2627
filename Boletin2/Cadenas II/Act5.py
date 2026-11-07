frase = input("Dime una frase: ")
palabraFinal = input("Dime una palabra que deberia terminar: ")
encontrado = False

if palabraFinal == frase[len(frase) - len(palabraFinal):]:
    encontrado = True
print(encontrado)