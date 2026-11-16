animales = ["gato", "perro", "capybara", "cuervo", "pez", "raton", "elefante"]

adiv_animal = input("Dime un animal: ")
cantidad_anim = len(animales) - 1
boleano = False
articulo = ""
i = 0

while i < cantidad_anim and not boleano:
    boleano = animales[i] == adiv_animal.lower()
    i += 1

if boleano:
    print(adiv_animal.lower() + " está en la lista")
else:
    print(adiv_animal.lower() + " no está en la lista")