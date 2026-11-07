costoPedido = int(input("Cuanto cuesta el pedido?: "))
tienePlus = input("Tienes la suscripción Plus? (S o N): ")

if costoPedido >= 35 or tienePlus.upper() == "S":
    gastosEnvio = False
    print("El envío es gratis")
else:
    gastosEnvio = True
    print("Tienes que pagar el envío")