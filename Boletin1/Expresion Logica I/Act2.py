anios = int(input("Cuantos años tienes: "))
pais = input("Cual país vives: ")

if anios > 18 and pais.lower() == "españa":
    print("Eres elegible para votar en las elecciones locales")
else:
    print("No cumples los requisitos")