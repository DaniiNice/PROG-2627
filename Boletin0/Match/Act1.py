num1 = int(input("Dime un numero: "))

match num1:
    case 0: 
        print("CERO")
    case 1: 
        print("UNO")
    case 2:
        print("DOS")
    case _:
        print("OTRAS")