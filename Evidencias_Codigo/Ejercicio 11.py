import random

# Generar lista con 20 números aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(20)]

# Mostrar la lista generada
print("Lista generada:")
print(lista)

# Inicializar mayor y menor con el primer valor
mayor = lista[0]
menor = lista[0]

# Buscar mayor y menor
for numero in lista:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

# Calcular la media entre mayor y menor
media = (mayor + menor) / 2

# Mostrar resultados
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Media entre mayor y menor: {media:.2f}")
