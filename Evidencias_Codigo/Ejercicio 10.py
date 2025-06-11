import random

# Generar la lista de 20 números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(20)]

# Mostrar la lista
print("Lista generada:")
print(lista)

# Calcular la suma manualmente
suma = 0
for numero in lista:
    suma += numero

# Calcular la media
media = suma / len(lista)

# Mostrar resultado
print(f"La suma total es: {suma}")
print(f"La media de los números es: {media:.2f}")
