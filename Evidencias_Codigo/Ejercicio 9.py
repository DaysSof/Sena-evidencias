import random

# Generar lista de 20 números aleatorios
lista = [random.randint(1, 100) for _ in range(20)]

# Mostrar la lista generada
print("Lista generada:")
print(lista)

# Leer número desde el teclado
numero_usuario = int(input("Ingrese un número: "))

# Calcular el número mayor
mayor = max(lista)

# Contar cuántas veces aparece el número mayor
contador_mayor = lista.count(mayor)

# Contar cuántas veces aparece el número ingresado por el usuario
contador_usuario = lista.count(numero_usuario)

# Mostrar resultados
print(f"El número mayor es: {mayor} y aparece {contador_mayor} vez/veces.")
print(f"El número ingresado ({numero_usuario}) aparece {contador_usuario} vez/veces.")

# Comparar apariciones
if contador_usuario > contador_mayor:
    print("Resultado: Verdadero (el número ingresado aparece más veces que el mayor).")
    print(True)
else:
    print("Resultado: Falso (el número ingresado no aparece más veces que el mayor).")
    print(False)
