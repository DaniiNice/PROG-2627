lista = ["Andrea", 5, "Pedro", 6, "Lucia", 3, "Paca", 9]

# Modifico el valor especifico de la lista
lista[5] = 5 
lista[4] = "Lucia Maria"

#print(f"{lista[4]} : {lista[5]}")

# Leemos y guardamos cuantos elementos tiene la lista
numeroElementos = len(lista)

# Contenido de la ultima posicion quitandole uno como for
#print(lista[numeroElementos-1])
# Numero de la ultima posicion
#print(numeroElementos)

lista.append(["Amparo", 6])
#print(lista)
#print(len(lista))

nombres = ["Andrea", "Lucia"]
notas = [6, 7]

nombres.append("Paco")
notas.append(5)

# Metodo 1
#print(f"{nombres[0]} : {notas[0]}")
#print(f"{nombres[1]} : {notas[1]}")
#print(f"{nombres[2]} : {notas[2]}")
# Metodo 2
#for posicion in range(len(nombres)):
#    print(f"{nombres[posicion]} : {notas[posicion]}")

print(lista[::-1]) # Dar la vuelta toda la lista