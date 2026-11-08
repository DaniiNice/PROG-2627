# El que necesita sangre
receptor = input("Dime el tipo de sangre del que recibe: ").upper()
# El que la da
emisor = input("Dime el tipo de sangre del donante: ").upper()

# Grupo A
if emisor == "A+":
    if receptor == "A+" or receptor == "AB+":
        print("Son compatibles")
    else:
        print("No son compatibles")
        
elif emisor == "A-":
    if receptor == "A+" or receptor == "A-" or receptor == "AB+" or receptor == "AB-":
        print("Son compatibles")
    else:
        print("No son compatibles")

# Grupo B
elif emisor == "B+":
    if receptor == "B+" or receptor == "AB+":
        print("Son compatibles")
    else:
        print("No son compatibles")
        
elif emisor == "B-":
    if receptor == "B+" or receptor == "B-" or receptor == "AB+" or receptor == "AB-":
        print("Son compatibles")
    else:
        print("No son compatibles")

# Grupo AB
elif emisor == "AB+":
    if receptor == "AB+":
        print("Son compatibles")
    else:
        print("No son compatibles")
        
elif emisor == "AB-":
    if receptor == "AB+" or receptor == "AB-":
        print("Son compatibles")
    else:
        print("No son compatibles")

# Grupo 0
elif emisor == "0+":
    if receptor == "A+" or receptor == "B+" or receptor == "AB+" or receptor == "O+" or receptor == "0+":
        print("Son compatibles")
    else:
        print("No son compatibles")
        
elif emisor == "0-":
    if receptor in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "0+", "0-"]:
        print("Son compatibles")
    else:
        print("No son compatibles")
        
else:
    print("Tipo de sangre del donante no reconocido.")