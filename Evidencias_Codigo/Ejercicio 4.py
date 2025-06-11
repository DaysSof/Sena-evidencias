# Solicitar los dos números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Asegurar que A sea menor que B
if a > b:
    a, b = b, a

#Sumar

suma = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        suma += i

#Mostrar resulatdo

print(f"La suma de los números pares entre {a} y {b} es: {suma}")