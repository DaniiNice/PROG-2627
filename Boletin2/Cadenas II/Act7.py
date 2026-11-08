nombreCompleto = input("Dime tu nombre completo: ")
nombreLista = nombreCompleto.split()

nombre = nombreLista[0]
apellido = nombreLista[1]
apellido2 = nombreLista[2]

nombreCompuesto = ""
nombreCompuesto += apellido[0].upper() + apellido[1:-1] + apellido[-1].upper() + " "
nombreCompuesto += apellido2[0].upper() + apellido2[1:-1] + apellido2[-1].upper() + " "
nombreCompuesto += nombre[0].upper() + nombre[1:-1] + nombre[-1].upper()

print(nombreCompuesto)