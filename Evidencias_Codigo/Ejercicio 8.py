import random

# Generar lista de 20 números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(20)]

# Mostrar la lista
print("Lista generada:")
print(lista)

# Encontrar el número mayor
mayor = max(lista)

# Contar cuántas veces aparece el número mayor
contador = lista.count(mayor)

# Mostrar resultados
print(f"El número mayor es: {mayor}")
print(f"Aparece {contador} vez/veces en la lista.")
