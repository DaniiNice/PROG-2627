dinero_gastado = int(input("Cuanto dinero gastaste en la tienda: "))
miembro = input("Eres miembro de lealtad? (S o N): ")

if dinero_gastado > 100 or miembro.lower() == "s":
    print("Eres elegible para descuentos en la tienda")
else:
    print("No cumples los requisitos")