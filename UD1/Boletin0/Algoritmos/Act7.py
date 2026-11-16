num1 = int(input("Dime un numero: "))
num2 = int(input("Dime otro numero: "))

if num1 > 0 and num2 > 0:
    print("Los 2 numeros son positivos")
elif num1 < 0 and num2 < 0:
    print("Los 2 numeros son negativos")
else:
    print("Uno es negativo y el otro es positivo")