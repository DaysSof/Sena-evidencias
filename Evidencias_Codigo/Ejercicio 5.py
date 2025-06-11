#Solicitar números
numeros = []

for i in range(1, 6):
    num = int(input(f"Ingrese el número {i}: "))
    numeros.append(num)

# Ordenar de mayor a menor
numeros.sort(reverse=True)

# Mostrar los números ordenados
print(f"Números ordenados de mayor a menor: {numeros}")