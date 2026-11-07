num1 = int(input("Dime un numero: "))
num2 = int(input("Dime otro numero: "))
num3 = int(input("Dime otro numero mas: "))

if num1 >= num2 and num2 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
    
print(f"El mayor de los tres números es: {mayor}")