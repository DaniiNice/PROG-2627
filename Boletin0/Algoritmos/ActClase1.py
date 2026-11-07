resultado = 3
num = int(input("Dame un numero: "))

if num % 2 == 0:
    print("Tu numero es par")
    resultado *= num

num += 1
resultado += num

print(resultado)