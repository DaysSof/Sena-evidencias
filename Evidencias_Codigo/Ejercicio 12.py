import random

# Generar lista de 20 números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(20)]

# Crear la lista inversa con reversed()
lista_inversa = list(reversed(lista))

# Mostrar resultados
print("Lista original:")
print(lista)

print("Lista inversa:")
print(lista_inversa)
