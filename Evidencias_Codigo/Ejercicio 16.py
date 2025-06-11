monedas = [1000, 500, 200, 100, 50]

valor_cobrar = int(input("Ingrese el valor a cobrar: "))
monto_entregado = int(input("Ingrese el monto entregado: "))

cambio = monto_entregado - valor_cobrar
 
if cambio < 0:
    print(f"Monto insuficiente. Faltan {cambio} pesos.")
elif cambio == 0:
    print("No hay cambio que devolver.")
else:
    print(f"Cambio a entregar: {cambio} pesos")
    for moneda in monedas:
        cantidad = cambio // moneda
        cambio = cambio % moneda
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de {moneda}")
