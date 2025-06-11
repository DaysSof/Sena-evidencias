import random

# Generar lista aleatoria de 20 números entre 1 y 100
lista = [random.randint(1, 100) for _ in range(20)]

def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Mostrar lista")
    print("2. Buscar número y mostrar posiciones")
    print("3. Contar cuántas veces aparece un número")
    print("4. Mostrar el número mayor y cuántas veces aparece")
    print("5. Ver si un número aparece más veces que el mayor")
    print("6. Calcular la media de todos los números")
    print("7. Calcular la media entre el mayor y el menor")
    print("8. Invertir la lista")
    print("0. Salir")
    print("------------------------")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Lista generada:")
        print(lista)

    elif opcion == "2":
        num = int(input("Ingrese el número a buscar: "))
        posiciones = [i for i, val in enumerate(lista) if val == num]
        if posiciones:
            print(f"El número {num} se encuentra en las posiciones: {posiciones}")
        else:
            print("Número no encontrado.")

    elif opcion == "3":
        num = int(input("Ingrese el número a contar: "))
        apariciones = lista.count(num)
        print(f"El número {num} aparece {apariciones} vez/veces.")

    elif opcion == "4":
        mayor = max(lista)
        apariciones = lista.count(mayor)
        print(f"El número mayor es {mayor} y aparece {apariciones} vez/veces.")

    elif opcion == "5":
        num = int(input("Ingrese el número a comparar: "))
        mayor = max(lista)
        apariciones_mayor = lista.count(mayor)
        apariciones_usuario = lista.count(num)
        print(f"El número mayor ({mayor}) aparece {apariciones_mayor} vez/veces.")
        print(f"El número ingresado ({num}) aparece {apariciones_usuario} vez/veces.")
        if apariciones_usuario > apariciones_mayor:
            print("Resultado: Verdadero.")
        else:
            print("Resultado: Falso.")

    elif opcion == "6":
        media = sum(lista) / len(lista)
        print(f"La media de todos los números es: {media:.2f}")

    elif opcion == "7":
        mayor = max(lista)
        menor = min(lista)
        media_extremos = (mayor + menor) / 2
        print(f"Mayor: {mayor}, Menor: {menor}")
        print(f"Media entre el mayor y el menor: {media_extremos:.2f}")

    elif opcion == "8":
        lista_inversa = list(reversed(lista))
        print("Lista original:")
        print(lista)
        print("Lista inversa:")
        print(lista_inversa)

    elif opcion == "0":
        print("Fin del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
