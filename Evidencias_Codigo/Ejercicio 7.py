import random

# Generar lista de 20 números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(20)]

# Mostrar la lista generada
print("Lista generada:")
print(lista)

# Leer el número a buscar
numero_buscado = int(input("Ingrese un número para buscar en la lista: "))

# Contar ocurrencias y mostrar posiciones
contador = 0

for i in range(len(lista)):
    if lista[i] == numero_buscado:
        print(f"Número encontrado en la posición {i}")
        contador += 1

# Mostrar resultados
if contador == 0:
    print("Número no encontrado.")
else:
    print(f"El número {numero_buscado} aparece {contador} vez/veces en la lista.")
