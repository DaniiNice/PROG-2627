compra = float(input("Precio del producto (negativo para terminar): "))
lista_compra = 0

while compra >= 0:
    lista_compra += compra
    compra = float(input("Precio del producto (negativo para terminar): "))

print("Total a pagar:", str(lista_compra) + "€")