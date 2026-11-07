num = int(input("Dime un numero: "))
num = str(num)
capicua = False

#for i in range(len(num)):
#    if num[i] == num[len(num) - 1 - i]:
#        capicua = True
#print(capicua)

if num == num[::-1]:
    capicua = True
print(capicua)