error = True

while error:
    num = int(input("Dime un numero (debe ser positivo): "))
    exponente = int(input("Dime un exponente (debe ser positivo): "))

    if num > 0 and exponente > 0:
        error = False

multiplicacion = num

for i in range(1, exponente):
    multiplicacion *= num
print(str(num) + "^" + str(exponente), "=", multiplicacion)