def calcular_raiz_cuadrada(numero):

    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")

    return numero ** 0.5

try:
    resultado = calcular_raiz_cuadrada(-9)

except ValueError as e:
    print(f"Error:{e}")