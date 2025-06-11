capital = float(input("Ingrese el capital del préstamo: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
años = int(input("Ingrese el número de años: "))

# Calcular tasa de interés mensual y número total de pagos
R = interes_anual / 100 / 12
N = años * 12

# Calcular cuota mensual
if R == 0:
    cuota_mensual = capital / N  # Sin intereses
else:
    cuota_mensual = (capital * R) / (1 - (1 + R) ** -N)

# Calcular el total a pagar
total_pagar = cuota_mensual * N

# Mostrar resultados
print(f"Cuota mensual: ${cuota_mensual:.2f}")
print(f"Total a pagar en {años} años: ${total_pagar:.2f}")
