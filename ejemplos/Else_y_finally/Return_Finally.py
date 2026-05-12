def dividir(a, b):

    try:
        resultado = a / b
        return resultado

    except ZeroDivisionError:
        print("Error: División por cero")
        return None

    finally:
        print("División finalizada")

print(dividir(10, 2))
print(dividir(10, 0))