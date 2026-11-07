compra = float(input("Precio del producto (negativo para terminar): "))
lista_compra = 0

while compra >= 0:
    lista_compra += compra
    compra = float(input("Precio del producto (negativo para terminar): "))

iva = lista_compra * 1.07

print("Total a pagar:", str(lista_compra) + "€")
print("Con 7% IVA incluido:", str(iva) + "€")