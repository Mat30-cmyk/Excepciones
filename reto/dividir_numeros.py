def dividir_numeros():

    try:
        # Solicita al usuario el primer número
        numero1 = input("Introduce el primer número: ")

        # Solicita al usuario el segundo número
        numero2 = input("Introduce el segundo número: ")

        # Convierte las entradas de texto a números enteros
        numero1 = int(numero1)
        numero2 = int(numero2)

        # Realiza la división entre los dos números
        resultado = numero1 / numero2

        # Muestra el resultado de la operación
        print(f"El resultado de la división es: {resultado}")

        # Retorna el resultado obtenido
        return resultado

    # Se ejecuta si el usuario escribe algo que no es un número
    except ValueError:
        print("Error: Debes introducir un número válido")

    # Se ejecuta si el usuario intenta dividir entre cero
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")

    # Este bloque siempre se ejecuta sin importar si hubo error o no
    finally:
        print("Operación finalizada")


# Llamada a la función
dividir_numeros()