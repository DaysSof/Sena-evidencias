import random

solucion = random.sample(range(10), 4)

intentos = 0

print("Bienvenido al juego Rojo-Amarillo-Verde.")
print("Debes adivinar 4 dígitos distintos entre 0 y 9.")
print("La pista por cada posición será: Verde (✔), Amarillo (⚠), Rojo (✘).")

while True:
    entrada = input("Ingresa tus 4 dígitos separados por espacio: ")
    intento = entrada.strip().split()

    if len(intento) != 4 or not all(d.isdigit() for d in intento):
        print("Entrada inválida. Asegúrate de ingresar exactamente 4 números.")
        continue

    intento = [int(d) for d in intento]

