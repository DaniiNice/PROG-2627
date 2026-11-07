error = True

while error:
    user = input("Usuario: ")

    if user == "usuario1":
        error = False
    else:
        print("Intentelo de nuevo...")

error = True

while error:
    password = input("Constraseña: ")

    if password == "inicio1234":
        print("Usuario logado correctamente")
        error = False
    else:
        print("Intentelo de nuevo...")