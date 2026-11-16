num = int(input("Dime un numero: "))

while num > 0:
    # Extraigo el ultimo num
    ultimo = num % 10
    print(ultimo)
    # Quito el ultimo num
    num = num // 10