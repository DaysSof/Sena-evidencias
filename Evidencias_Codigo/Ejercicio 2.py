#Ingresar un número

while True:
    try:
        N = int(input("Ingresar un número"))
        suma = 0
        
#Calcular la suma

        for i in range(1, N + 1):
            suma += i
            
#Mostrar resultados

        print(f"La suma es: {suma}")
        break
    except:
        print("Opción no válida")