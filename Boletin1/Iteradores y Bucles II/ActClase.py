edad = int(input("Introduzca su edad para saber si le corresponde el bono cultural"))

while edad < 18:
    if edad > 0:
        edad = int(input("Introduzca su edad para saber si le corresponde el bono cultural"))
    elif edad > 17:
        print("enhorabuena!")