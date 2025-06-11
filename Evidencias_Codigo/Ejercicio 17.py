aprendices = [
    "Aguilar", "Benítez", "Cabrera", "Díaz", "Espinosa",
    "Fernández", "García", "Herrera", "López", "Martínez"
]

print("Lista original de aprendices:")
for apellido in aprendices:
    print(apellido)

nuevo_aprendiz = input("Ingrese el apellido del nuevo aprendiz: ")

aprendices.append(nuevo_aprendiz)
aprendices.sort()

print("Lista actualizada de aprendices:")
for apellido in aprendices:
    print(apellido)
