def ConvertirEspaciado (text):
    cadena = ""

    for i in range(len(text)):
        if text[i] != " ":
            cadena += text[i] + " "
    return cadena

frase = input("Dime una frase: ")
print(ConvertirEspaciado(frase))