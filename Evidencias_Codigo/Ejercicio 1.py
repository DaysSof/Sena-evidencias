#Ingresar número

while True:
    try:
        a = int(input("Ingresar un número"))
        break
    except:
        print("Opción no válida")


#Definir si es par

if a % 2 == 0:
    print(f"El núero {a} es par.")
else:
    print(f"El núero {a} es impar.")