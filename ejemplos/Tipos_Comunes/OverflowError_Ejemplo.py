try:
    resultado = 10.0 ** 1000000
except OverflowError:
    print("El número es demasiado grande para ser representado")