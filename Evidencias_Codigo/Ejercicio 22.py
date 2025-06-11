import random

def generar_codigo():
    return random.sample(range(10), 4)  # 4 dígitos distintos

def evaluar_intento(codigo_secreto, intento):
    verdes = 0
    amarillos = 0
    rojos = 0

    for i in range(4):
        if intento[i] == codigo_secreto[i]:
            verdes += 1
        elif intento[i] in codigo_secreto:
            amarillos += 1
        else:
            rojos += 1

    return verdes, amarillos, rojos

def jugar():
    codigo_secreto = generar_codigo()
    intentos = 0

    print("Bienvenido al juego Rojo-Amarillo-Verde (Versión difícil)")
    print("Adivina los 4 dígitos en la posición correcta.")
    print("Introduce 4 dígitos del 0 al 9, distintos entre sí.")
    print("Solo se mostrará cuántos dígitos son 'Verde', 'Amarillo' o 'Rojo'.")

    while True:
        entrada = input("Ingresa tus 4 dígitos: ").strip()

        if len(entrada.replace(" ", "")) == 4:
            intento = [int(c) for c in entrada if c.isdigit()]
        else:
            print("Entrada inválida. Asegúrate de escribir exactamente 4 dígitos.")
            continue

        if len(intento) != 4 or len(set(intento)) != 4:
            print("Los dígitos deben ser 4 y distintos entre sí, del 0 al 9.")
            continue

        intentos += 1
        verdes, amarillos, rojos = evaluar_intento(codigo_secreto, intento)

        print(f"Pista: {verdes} Verde(s), {amarillos} Amarillo(s), {rojos} Rojo(s)\n")

        if verdes == 4:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            print("El código era:", codigo_secreto)
            break

if __name__ == "__main__":
    jugar()
