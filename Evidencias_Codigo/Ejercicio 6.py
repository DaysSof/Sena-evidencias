import random

# Generar lista de 20 números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(20)]

# Mostrar la lista
print("Lista generada:")
print(lista)

# Leer el número a buscar
numero_buscado = int(input("Ingrese un número para buscar en la lista: "))

# Buscar el número en la lista
encontrado = False

for i in range(len(lista)):
    if lista[i] == numero_buscado:
        print(f"Número encontrado en la posición {i}")
        encontrado = True

if not encontrado:
    print("Número no encontrado.")