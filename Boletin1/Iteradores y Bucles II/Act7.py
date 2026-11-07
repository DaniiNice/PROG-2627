num = int(input("Dime un numero (0 para terminar): "))
num2 = int(input("Dime otro numero (0 para terminar): "))

while num != 0 and num2 != 0:
    print(f"Su suma es: {num + num2}")
    num = int(input("Dime un numero (0 para terminar): "))
    num2 = int(input("Dime otro numero (0 para terminar): "))