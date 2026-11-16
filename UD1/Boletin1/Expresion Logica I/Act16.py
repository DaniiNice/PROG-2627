# Creamos las listas para almacenar múltiples productos
nuevos = []
mas_vendidos = []
oferta = []

while True:
# -- Codigo que hacemos al menos una vez --
    nombre_producto = input("Dime el nombre del producto: ")

    dia = int(input("Dime el dia numerico del producto: "))
    mes = int(input("Dime el mes del producto: "))
    anio = int(input("Dime el año del producto: "))

    # Cambiamos el formato de la fecha
    fecha_formato = f"{dia}/{mes}/{anio}"
    # Creamos una clave oculta año-mes-día para que Python pueda ordenar las fechas correctamente
    # Rellenamos con ceros (zfill) para que el mes 5 sea "05" y no falle el orden alfabético
    fecha_orden = f"{anio}-{str(mes).zfill(2)}-{str(dia).zfill(2)}"

    ventas = int(input("Dime las ventas totales del producto: "))
    descuento = input("El producto tiene descuentos aplicados? (S o N): ")

    # Añadimos un diccionario nuevo a cada lista por cada registro

    nuevos.append({"Producto": nombre_producto, "Fecha": fecha_formato, "orden": fecha_orden})
    mas_vendidos.append({"Producto": nombre_producto, "Ventas": ventas})
    oferta.append({"Producto": nombre_producto, "Oferta": descuento.upper()})

    stop = input("Parar de registrar productos? (S o N): ")

# -- Condicion para salir del bucle --
# Importante recordar: Añadidos los paréntesis () a .lower()
    if stop.upper() == "S":
        break

# -- Logica de orden --
# 1. Ordenar mas nuevos: Ordena por la clave oculta "orden" de mayor a menor
nuevos.sort(key=lambda x: x["orden"], reverse=True)
# 2. Ordenar mas vendidos: Ordena por la clave "Ventas" de mayor a menor
mas_vendidos.sort(key=lambda x: x["Ventas"], reverse=True)

# -- Impresion Visual --
print("\n--------------------------------")
print("Tabla de Productos Registrados")
print("--------------------------------")

print("\n📅  Productos más nuevos:")
for p in nuevos:
    print(f"  • {p['Producto']} - Registrado el: {p['Fecha']}")

print("\n🔥  Productos más vendidos:")
for p in mas_vendidos:
    print(f"  • {p['Producto']} - Ventas: {p['Ventas']} unidades")

print("\n🏷️  Productos en oferta:")
for p in oferta:
    # Cambiamos la "S" y "N" para que sea mas visible
    estado_oferta = "Sí" if p['Oferta'] == "S" else "No"
    print(f"  • {p['Producto']} - ¿Tiene descuento?: {estado_oferta}")